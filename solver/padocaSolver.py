# -*- coding: utf-8 -*-
########## padocaSolver.py ##########

#run => python padocaSolver.py instance.padoca [timelimit]

import localsolver
import sys


def readPadocaInstance(nAbastecedores, nClientes, custoA, custoAtoC, arqName):
    file = open(arqName, "r", encoding="utf-8")

    for line in file.readlines():
        tokens = line.split()
        if( len(tokens) == 0 ):
            continue
        id = tokens[0]
        if( id == "p" ):
            nClientes, nAbastecedores = map(int, [tokens[2], tokens[3]])
            custoA = []
            for i in range(nAbastecedores):
                custoA.append(0)
            custoAtoC = []
            for i in range(nClientes):
                custoAtoC.append([])
                for j in range(nAbastecedores):
                    custoAtoC[i].append(0)
        elif( id == "w" ):
            c, a = map(int, [tokens[1], tokens[2]])
            c -= 1
            a -= 1
            (custoAtoC[c])[a] = float(tokens[3])
        elif( id == "v" ):
            a = int(tokens[1])
            a -= 1
            custoA[a] = float(tokens[2])
        elif( id == "c" ):
            #comentarios, apenas ignorar
            pass
        else:
            raise Exception('Formato incorreto de instância, leia o readme')
    return nAbastecedores, nClientes, custoA, custoAtoC

with localsolver.LocalSolver() as ls:

    #
    # Declares the optimization model
    #
    model = ls.model

    if len(sys.argv) < 2:
        print("Usage: python padocaSolver.py instance.padoca [timelimit]")
        sys.exit(1)

    nAbastecedores = None
    nClientes      = None
    custoA         = None
    custoAtoC      = None

    nAbastecedores, nClientes, custoA, custoAtoC = readPadocaInstance(nAbastecedores, nClientes, custoA, custoAtoC, sys.argv[1])     

  

    # Variável X_ij
    # o cliente i esta sendo abstecido pelo abastecedor j x[i][j]
    x = []
    for i in range(nClientes):
        x.append([])
        for j in range(nAbastecedores):
            x[i].append(model.int(0,1))
            x[i][j].name = "x"+str(i)+str(j)

    # Variável Y_i
    # Se o abstecedor i foi utilizado
    y = []
    for i in range(nAbastecedores):
        y.append(model.int(0,1))
        y[i].name = "y"+str(i)


    # Restrição de cobertura
    for c in range(nClientes):
        clientRestr = 0
        for a in range(nAbastecedores):
            clientRestr += (x[c])[a]
        model.constraint(clientRestr >= 1)

    # Forçar ativação de variáveis y
    for a in range(nAbastecedores):
        absRestr = 0
        absRestr += nClientes*y[a]
        for c in range(nClientes):
            absRestr -= (x[c])[a]
        model.constraint(absRestr >= 0)

    # Função Objetivo
    custoAloc = 0
    #soma dos custos de ativação
    for a in range(nAbastecedores):
        custoAloc += custoA[a]*y[a]

    #soma das alocações de cada cliente c
    for c in range(nClientes):
        for a in range(nAbastecedores):
            custoAloc += (custoAtoC[c])[a]*(x[c])[a]
    model.minimize(custoAloc)

    model.close()

    ############################################################
    #######                 Parametros                  ########
    ############################################################
    if len(sys.argv) >= 3: ls.param.time_limit = int(sys.argv[2])
    else: ls.param.time_limit = 2

    ls.solve()

    #
    # Writes the solution in a file with the following format:
    #  - surface and volume of the bucket
    #  - values of R, r and h
    #
    print( custoAloc)
    #print("%d %d %d %d\n" % (anel.value, tv.value, livro.value, vinho.value))
    
    sol = []
    for c in range(nClientes):
        sol.append(-1)

    for c in range(nClientes):
        for a in range(nAbastecedores):
            if( x[c][a].value == 1 ):
                sol[c] = a

    #print(sol)
    arqOut = sys.argv[1]
    arqOut = arqOut.replace(".padoca",".prun").replace("PadocaInstances", "PadocaRuns")
    print("arqOut: ", arqOut)
    output = open(arqOut, "w", encoding="utf-8")

    output.write("{")
    output.write("\"custo\":\""+str(custoAloc.value)+"\"," )

    output.write("\"solucao\":[")
    for i in range(len(sol)):
        if( i == len(sol)-1 ):
            output.write("\""+str(sol[i])+"\"],")
        else:
            output.write("\""+str(sol[i])+"\", ")
    output.write("\"encerrado\": \"true\"")
    output.write("}")

    
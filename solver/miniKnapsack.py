# -*- coding: utf-8 -*-
########## miniKnapsack.py ##########

import localsolver
import sys

with localsolver.LocalSolver() as ls:

    #
    # Declares the optimization model
    #
    m = ls.model

    # Variáveis
    anel  = m.int(0, 1)
    tv    = m.int(0, 1)
    livro = m.int(0, 1)
    vinho = m.int(0, 1)
 
    pesoAnel  = 0.5
    pesoTv    = 10
    pesoLivro = 2
    pesoVinho = 4

    valorAnel  = 10
    valorTv    = 5
    valorLivro = 2
    valorVinho = 3


    # Tamanho da mochila
    L = 10

    # Restrições
    mochila = pesoAnel*anel + pesoTv*tv + pesoLivro*livro + pesoVinho*vinho
    m.constraint(mochila <= L)

    # Função Objetivo
    valorMochila = valorAnel*anel + valorTv*tv + valorLivro*livro + valorVinho*vinho
    m.maximize(valorMochila)

    m.close()

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
    print("%f \n" % (valorMochila.value))
    print("%d %d %d\n" % (anel.value, tv.value, livro.value, vinho.value))
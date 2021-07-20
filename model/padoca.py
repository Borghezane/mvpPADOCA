#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tools.pwGenerator import PwGenerator
import os

class Padoca(): 
    id = 0
    init = False

    def getUpdateId():
        envArq = open("padoca.env","r+", encoding="utf-8")

        for line in envArq.readlines():
            elements = line.split(" ")
            if( elements[0] == "id" ):
                Padoca.id = int(elements[1])
                envArq.close()
                Padoca.init = True
                return True
        return False

    def setUpdateId():
        if(Padoca.init == False):
            raise Exception('Arquivo não inicializado, tente executar getUpdateId antes de utilizar a classe Padoca')

        envArq = open("padoca.env","r", encoding="utf-8")

        envStr = ""
        for line in envArq.readlines():
            elements = line.split(" ")
            if( elements[0] == "id" ):
                envStr += "id "+str(Padoca.id)+"\n"
            else:
                envStr += line 
        envArq.close()

        envArq = open("padoca.env","w", encoding="utf-8")

        envArq.write(envStr)
        envArq.close()





    def __init__(self, nClientes, nFornecedores, custoFornecedorCliente, custoFornecedor):
        self.id                     = None 
        self.nClientes              = nClientes
        self.nFornecedores          = nFornecedores
        self.custoFornecedorCliente = custoFornecedorCliente
        self.custoFornecedor        = custoFornecedor
        self.password               = None
        self.arqName                = None


        self.id = Padoca.id
        Padoca.id     += 1 
        Padoca.setUpdateId()
        self.arqName = "data/PadocaInstances/"+str(self.id)+".padoca"
        #self.arquivo = open("PadocaInstances/"+str(self.id)+".padoca","a+", encoding="utf-8")
        self.password = PwGenerator.genPw(16)
        



    def run(self):
        pid = None
        #createFileInstance(self)
        #chamar resolvedor
        # pid = solv(self) bla bla bla


        if os.name == "posix":
            os.system("python solver/padocaSolver.py " + self.arqName + " &") 
        else:
            os.system("start /B python solver/padocaSolver.py " + self.arqName )


        pid = 13
        return pid
        
    def getPassword(self):
        return self.password

    def createFileInstance(self):
        arq = open("data/PadocaInstances/"+str(self.id)+".padoca","a+", encoding="utf-8")

        problemStr = "p padoca " + str(self.nClientes) + " " + str(self.nFornecedores) + "\n"
        
        wStr = ""
        for i in range(self.nClientes):
            for j in range(self.nFornecedores):
                wStr += "w " + str(i+1) + " " + str(j+1) + " " + str((self.custoFornecedorCliente[i])[j]) + "\n"
        vStr = ""
        for i in range(self.nFornecedores):
            vStr += "v " + str(i+1) + " " + str(self.custoFornecedor[i]) + "\n"

        arq.write(problemStr)
        arq.write(wStr)
        arq.write(vStr)

        arq.close()


    def checkPass(self, password):
        return self.password == password

    def getSol(self):
        pass

if __name__ == '__main__':
    Padoca.getUpdateId()
    #padoquinha = Padoca()
    #padoquinha2 = Padoca()  



    nClientes = 5
    nFornecedores = 3

    custoFornecedorCliente = []
    for i in range(nClientes):
        custoFornecedorCliente.append([])
        for j in range(nFornecedores):
            custoFornecedorCliente[i].append(1)

    custoFornecedor = []
    for i in range(nFornecedores):
        custoFornecedor.append(1)

    padoquinha = Padoca(nClientes, nFornecedores, custoFornecedorCliente, custoFornecedor)

    padoquinha.createFileInstance()


    #print(padoquinha2.id)

    #Padoca.setUpdateId()


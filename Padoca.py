#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwGenerator import *

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




    
    def __init__(self):
        self.id                     = None 
        self.nClientes              = None
        self.nFornecedores          = None
        self.custoFornecedorCliente = None
        self.custoFornecedor        = None
        self.password               = None
        self.arquivo                = None


        self.id = Padoca.id
        self.arquivo = open("PadocaInstances/"+str(self.id)+".padoca","a+", encoding="utf-8")
        self.password = pwGenerator.genPw(16)
        Padoca.id     += 1 
        pass

    def run(self):
        pid = None
        #createFileInstance(self)
        #chamar resolvedor
        # pid = solv(self) bla bla bla
        pid = 13
        return pid

    def createFileInstance(self):
        pass

    def checkPass(self):
        pass

    def getSol(self):
        pass

if __name__ == '__main__':
    Padoca.getUpdateId()
    padoquinha = Padoca()
    #padoquinha2 = Padoca()  



    #print(padoquinha2.id)

    Padoca.setUpdateId()


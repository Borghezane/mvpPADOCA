#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Instancias():
    padocas = {}

    def addPadoca(padoca, padId):
        Instancias.padocas[padId] = padoca

    def getPadoca(id):
        return Instancias.padocas[id]

    def getPadocaPorSenha(padSenha):
        return None 

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 22:14:24 2021

@author: Raquel
"""

import numpy as np

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0, 0, 0, 1])
pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if (soma >= 1):
        return 1 
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while (erroTotal != 0 ):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.array(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('peso atualizado: ' + str(pesos[j]))
            print('total de erros: ' + str(erroTotal))
            
treinar()
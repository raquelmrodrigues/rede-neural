# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 00:04:26 2021

@author: Raquel
"""

import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):           #da o direcionamento para o calculo dos pesos
    return sig * (1 - sig)

a = sigmoid(0.5)
b = sigmoidDerivada(a)

entrada = np.array([[0,0],[0,1],[1,0],[1,1]])
saida = np.array([[0],[1],[1],[0]])

peso0 = np.array([[-0.424, -0.740, -0.961],
                 [0.358, -0.577, -0.469]])

peso1 = np.array([[-0.017],[-0.893],[0.148]])

epocas = 100
for j in range(epocas):
    camadaEntrada = entrada
    somaSinapse0 = np.dot(camadaEntrada, peso0)
    camadaOculta = sigmoid(somaSinapse0)
    
    somaSinapse1 = np.dot(camadaOculta, peso1)
    camadaSaida = sigmoid(somaSinapse1)
    
    erroCamdaSaida = saida - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamdaSaida))
    
    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamdaSaida * derivadaSaida
    
    peso1Transposta = peso1.T
    deltaSaidaxPeso = deltaSaida.dot(peso1Transposta)
    deltaCamadaOculta = deltaSaidaxPeso * sigmoidDerivada(camadaOculta)
    
    
    
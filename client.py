#Aqui vocês irão colocar seu algoritmo de aprendizado
import numpy as np
import connection as cn
import random

s = cn.connect(2037)
act = ["left", "right", "jump"]                 #A ordem das colunas na Q-Table de ser
                                                #Giro pra esquerda, Girot pra direita, Pulo pra frente
Qtable = np.zeros(96, len(act))

#Hyperparametros Alpha, Gamma e Epsilon. Optei por iniciar comm valores padrao abaixo

alpha = 0.01
gamma = 0.9
epsilon = 0.1

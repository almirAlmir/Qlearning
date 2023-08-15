#Aqui vocês irão colocar seu algoritmo de aprendizado
import numpy as np
import connection as cn
import random

act = ["left", "right", "jump"]     #A ordem das colunas na Q-Table de ser
                                    #Giro pra esquerda, Giro pra direita, Pulo pra frente


#Hyperparametros Alpha, Gamma e Epsilon. Optei por iniciar com valores padrao abaixo

alpha = 0.3
gamma = 0.8
epsilon = 0.4

state = 0

wins = 0
reward = 0

def write_txt(q_tabel):
    
    lines = q_tabel
    
    with open("resultado.txt", "w") as file:
        
        for line in lines:
            text = " ".join(str(i) for i in line) #concatena o texto com " "
            file.write(text + "\n") #quebra linha
            
    file.close()

def read_txt(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        q_tabel = [list(map(float, line.strip().split())) for line in lines]
    return q_tabel

Qtable = read_txt("resultado.txt")
print(Qtable)
    
s = cn.connect(2037)
total_interactions = 1000
for i in range (1, total_interactions):
    print('rodada', i)
    
    finished = False
    
    while not finished:
        
        action = 0
        
        if random.uniform(0, 1) < epsilon:
            print('random epsilon', epsilon)
            action = random.randint(0, 2) #Uma das 3 açoes: left, right, jump
        else:
            print('not random')
            value = -1000 #valor arbitrario
            for index in range (3): #percorre as acoes de 0 até 2
                    
                if Qtable[state][index] > value:
                    action = index
                    value = Qtable[state][index]
                    
        current_state = state
        state, reward = cn.get_state_reward(s , act[action])
        print('reward', reward)
        state = int(state, 2) #S2
        print('state', state)
        
        #Equação de Bellman para atualização da Tabela_Q
        estimate = reward + gamma*np.max(Qtable[state]) #Estimativa de Q(s,a) pela Equação de Belman
        erro = estimate - Qtable[current_state][action] #Estimativa - Valor atual
        Qtable[current_state][action] += alpha * erro #nomes escolhidos de acordo com slides

        if reward == 300 or reward <= -100:
            if reward == 300:
                wins+=1
            finished = True
            break
    
    epsilon -= (epsilon/total_interactions)
    print('wins', wins)
    write_txt(Qtable)                
                    

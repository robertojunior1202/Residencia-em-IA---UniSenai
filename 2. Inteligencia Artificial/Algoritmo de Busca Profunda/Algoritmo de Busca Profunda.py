import pandas as pd
from libs_roberto_junior import estrategiaAdjacencia
#Importando Labirinto
caminho = 'IA_2_labirinto256.txt'
df = pd.read_csv(caminho, sep=" ", header=None)

#Parâmetros de Configuração
posicao_atual = 0,0
estrategia = "ea10"

#Loop Infinito
cont = 0
fila2 = []
visitas = [[0,0]]
encontrado = False
while True:
    fila = []
    regra = estrategiaAdjacencia(posicao_atual, estrategia)  
    for posicao in regra:
        #Capta as informações adjacentes e armazena na pilha
        if 0<=posicao[0]<=255 and 0<=posicao[1]<=255:
            valor = df.iloc[posicao[0],posicao[1]]
            if valor == -1:
                print(f'Objetivo encontrado. O valor de -1 está na posição {[posicao[0],posicao[1]]}')
                encontrado = True
            elif valor == 1:
                fila.append([posicao[0],posicao[1]])
    
    if encontrado:
        break
    #Organizando os dados em pilha
    for dado in reversed(fila):
        if dado not in fila2:
            fila2.append(dado)
                
    #Organiza a movimentação
    posicao_atual = fila2[-1]  #capta próxima posição
    fila2.remove(posicao_atual)
    visitas.append(posicao_atual)
    df.iloc[posicao_atual[0],posicao_atual[1]]=255 #marca 255 na posição visitada  
    cont+=1
    
print(f'O problema foi encontrado com {cont} iterações')
       
     
  


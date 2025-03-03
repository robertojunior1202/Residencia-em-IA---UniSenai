import pandas as pd
#from libs_roberto_junior import estrategiaAdjacencia
#Importando Labirinto
caminho = 'IA_2_labirinto256.txt'
df = pd.read_csv(caminho, sep=" ", header=None)



#implementar lista de posições visitadas
#implementar pilha apenas casas que atendem a regra
#deslocar para a melhor posição
#marcar posição deslocada
#captar dados das posições adjacentes

#Parâmetros de Configuração
posicao_atual = 0,0
estrategia = "ea1"

#Desmembrar depois
def estrategiaAdjacencia(posicao_atual, estrategia):
    #Regra de Posições
    L = posicao_atual[0],posicao_atual[1]+1
    SL = posicao_atual[0]+1,posicao_atual[1]+1
    S = posicao_atual[0]+1,posicao_atual[1]
    SO = posicao_atual[0]+1,posicao_atual[1]-1
    O = posicao_atual[0],posicao_atual[1]-1
    NO = posicao_atual[0]-1,posicao_atual[1]-1 
    N = posicao_atual[0]-1,posicao_atual[1]
    NL = posicao_atual[0]-1,posicao_atual[1]+1

    #Regra de Estratégias
    if estrategia == "ea1": #ea1 - SL-L-NL-N-NO-O-SO-S
        regra = [SL,L,NL,N,NO,O,SO,S]
        return regra
    elif estrategia  == "ea2": #ea2 - S-SL-L-NL-N-NO-O-SO
        regra = [S,SL,L,NL,N,NO,O,SO]
        return regra
    elif estrategia  == "ea3": #ea3 - L-SL-S-NL-N-SO-O-NO
        regra = [L,SL,S,NL,N,SO,O,NO]
        return regra
    elif estrategia  == "ea4": #ea4 - SL-L-S-NL-N-SO-O-NO
        regra = [SL,L,S,NL,N,SO,O,NO]
        return regra
    elif estrategia  == "ea5": #ea5 - SL-L-S-NL-N-SO-NO-O
        regra = [SL,L,S,NL,N,SO,NO,O]
        return regra
    elif estrategia  == "ea6": #ea6 - SL-L-S-NL-N-O-NO-SO
        regra = [SL,L,S,NL,N,O,NO,SO]
        return regra
    else:
        return print(f'Estratégia {estrategia} é inválida. Escolha entre ea1 até ea6')

regra = estrategiaAdjacencia(posicao_atual, estrategia)


#Loop Infinito
cont = 0
pilha = []
visitas = [[0,0]]
while True:
    for posicao in regra:
        #Capta as informações adjacentes e armazena na pilha
        if 0<=posicao[0]<=255 and 0<=posicao[1]<=255:
            valor = df.iloc[posicao[0],posicao[1]]
            if valor == 1:
                pilha.append([posicao[0],posicao[1]])

    #Organiza a movimentação
    posicao_atual = pilha[0]  #capta próxima posição
    pilha.remove(posicao_atual)
    visitas.append(posicao_atual)
    df.iloc[posicao_atual[0],posicao_atual[1]]=255 #marca 255 na posição visitada  
    regra = estrategiaAdjacencia(posicao_atual, estrategia)     
     

#implementar ajusta por pilha. Captar as posições e passar pra pilha     

posicao = 0,0
import pandas as pd
import random
import math

#carregando o arquivo de id, lat long que é o .tsp
def carregaArquivoTSP(caminho, skiprows,cabecalho):
    data = pd.read_csv(caminho,
                    delim_whitespace=True, 
                    skiprows=skiprows, 
                    names=cabecalho)
    #Tratando df
    data = data[:-1]
    return data


#Gera aleatoriamente uma população inicial
def geraPopulacao(qtd, df, ponto_inicio=None): #passa a quantidade, o df .tsp e o ponto incio (opcional)
    populacao_inicial = []
    if ponto_inicio == None:
        for i in range(qtd):
            vetor_aleatorio = random.sample(range(1, len(df)+1), len(df))
            vetor_aleatorio.append(vetor_aleatorio[0])
            populacao_inicial.append(vetor_aleatorio)
        return populacao_inicial
    
    else:
        for i in range(qtd):
            vetor = []
            while len(vetor) < len(df)-1:
                valor = random.randint(1, len(df))
                if valor != ponto_inicio:
                    vetor.append(valor)
            vetor_aleatorio = [ponto_inicio] + vetor
            vetor_aleatorio.append(vetor_aleatorio[0])
            populacao_inicial.append(vetor_aleatorio)
        return populacao_inicial
   
   
     
     
df = carregaArquivoTSP("ALL_tsp/att48.tsp/att48.tsp",6,["ID", "Latitude", "Longitude"]) #Apagar depois de finalizado
population = geraPopulacao(1000, df,9) #Apagar depois de finalizado


#Calculando Fitness, qualificando e encontrando the best
def calculaFitness(populacao,df, qtd_selecao, the_best):
    populacao_qualify = {} 
    #Calcula Fitness
    for rota in populacao:
        dist = 0
        for i in range(len(rota)-1):
            saida = df[df["ID"] == str(rota[i])]
            chegada = df[df["ID"] == str(rota[i+1])]
            distancia = math.sqrt(
                (int(chegada["Latitude"].iloc[0])-int(saida["Latitude"].iloc[0]))**2 +\
                (int(chegada["Longitude"].iloc[0])-int(saida["Longitude"].iloc[0]))**2 
                                  )
            dist+=distancia
        populacao_qualify[dist] = rota
        
    #Avaliando Fitness
    selecao = []
    for chave, valor in populacao_qualify.items():
        fitness = 1/chave
        
        if len(selecao) <qtd_selecao: #verifico se já tenho a qtd mínima de the best
            selecao.append((fitness,chave, valor))
            selecao.sort() # Ordena para garantir que o menor esteja sempre no índice 0
        else:
            if fitness > selecao[0][0]:  
                selecao[0] = (fitness, chave, valor)  # Substitui o pior pelo novo melhor
                selecao.sort()  # Ordena novamente
    
    #Validando The Best
    if len(the_best)>0:
        if selecao[-1][0]>the_best[0][0]:
            the_best[0]=selecao[-1]
    elif len(the_best)==0: 
        the_best.append(selecao[-1])
        
    return populacao_qualify, selecao, the_best

the_best = []
#calculaFitness(population,df,10, the_best)    
populacao_qualify, selecao, the_best = calculaFitness(population,df,10,the_best) 


#TRABALHAR NO CROSSOVER
def crossover(selecao):
    selecao_crossover = []
    ponto_crossover = random.randint(1, len(selecao[0][2]) - 1)
    for pai in range(len(selecao)-1):
        filho1 = selecao[pai][2][:ponto_crossover] + selecao[pai+1][2][ponto_crossover:]
        filho2 = selecao[pai+1][2][:ponto_crossover] + selecao[pai][2][ponto_crossover:]
        selecao_crossover.append(filho1)
        selecao_crossover.append(filho2)

    return selecao_crossover

selecao_crossover = crossover(selecao)







#Faço a seleção (torneio, roleta, etc)
#Cruzamento crossover
#mutação
#defino um critério de parada para finalizar o script



#ANOTAÇÕES
#A primeira população ao passar no calculaFitness é random, a segunda em diante é a seleção + mutação + random (opcional ou programavel)
#Passar The Best inicial (vazio) no calculaFitness

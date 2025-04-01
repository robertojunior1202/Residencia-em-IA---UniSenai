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
    
    if ponto_inicio is None:
        # Quando não há ponto inicial, gera-se aleatoriamente sem repetições
        for i in range(qtd):
            vetor_aleatorio = random.sample(range(1, len(df) + 1), len(df))
            vetor_aleatorio.append(vetor_aleatorio[0])  # Fechar o ciclo
            populacao_inicial.append(vetor_aleatorio)
        return populacao_inicial
    
    else:
        # Quando há ponto inicial, garante-se que o ponto_inicio não se repita
        for i in range(qtd):
            vetor = [ponto_inicio]
            numeros_usados = {ponto_inicio}  # Usar um set para evitar repetições
            
            while len(vetor) < len(df):
                valor = random.randint(1, len(df))
                if valor != ponto_inicio and valor not in numeros_usados:
                    vetor.append(valor)
                    numeros_usados.add(valor)  # Marca o valor como usado
            
            vetor.append(vetor[0])  # Fechar o ciclo, repetindo o ponto inicial
            populacao_inicial.append(vetor)
        return populacao_inicial
   
   
     
     
df = carregaArquivoTSP("ALL_tsp/att48.tsp/att48.tsp",6,["ID", "Latitude", "Longitude"]) #Apagar depois de finalizado
population = geraPopulacao(1000, df,9) #Apagar depois de finalizado


#Calculando Fitness, qualificando e encontrando the best
def calculaFitness(populacao,df, qtd_selecao):
    the_best = []
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
    
    #Captando o The Best
    the_best.append(selecao[-1])
        
    return populacao_qualify, selecao, the_best

#the_best = []
#calculaFitness(population,df,10)    
populacao_qualify, selecao, the_best = calculaFitness(population,df,10) 


#TRABALHAR NO CROSSOVER e MUTAÇÃO
def embaralhar_crossover(lista):
    # Fixar o primeiro e o último valor
    inicio = lista[0]
    fim = lista[-1]
    
    # Obter os elementos do meio para embaralhar
    meio = lista[1:-1]
    
    # Embaralhar o meio
    random.shuffle(meio)
    
    # Montar a nova lista com os valores fixos no início e no final
    lista_crossover = [inicio] + meio + [fim]
    return lista_crossover


def crossover(selecao, df):
    selecao_crossover = []
    pai  = 0
    for pai in range(len(selecao)-1):
        filho1 = selecao[pai][2]
        filho2 = selecao[pai+1][2]
        
        filho1_cross = embaralhar_crossover(filho1)
        filho2_cross = embaralhar_crossover(filho2)
        filho3_cross = embaralhar_crossover(filho2)
        filho4_cross = embaralhar_crossover(filho1)
        
        #filho5_cross = geraPopulacao(1, df)
        #filho6_cross = geraPopulacao(1, df)
    
        selecao_crossover.append(filho1_cross)
        selecao_crossover.append(filho2_cross)
        selecao_crossover.append(filho3_cross)
        selecao_crossover.append(filho4_cross)
        #selecao_crossover.append(filho5_cross)
        #selecao_crossover.append(filho6_cross)

    return selecao_crossover

selecao_crossover = crossover(selecao,df)







#Faço a seleção (torneio, roleta, etc)
#Cruzamento crossover
#mutação
#defino um critério de parada para finalizar o script



#ANOTAÇÕES
#A primeira população ao passar no calculaFitness é random, a segunda em diante é a seleção + mutação + random (opcional ou programavel)
#Passar The Best inicial (vazio) no calculaFitness

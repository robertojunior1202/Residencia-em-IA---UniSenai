from functions import carregaArquivoTSP, geraPopulacao, calculaFitness, crossover

#Implementações Iniciais
caminho="ALL_tsp/att48.tsp/att48.tsp"
skiprows= 6
cabecalho = ["ID", "Latitude", "Longitude"]
qtd_populacao_inicial = 1000
ponto_inicial = 1
the_best = []
qtd_iteraçoes = 1000
x = 0
x_the_best = 0



#Carrego arquivo
#Function importação .TSP
df = carregaArquivoTSP(caminho,skiprows,cabecalho)

#Gero população aleatorio inicial
#passa a quantidade, o df .tsp e o ponto inicial (opcional)
#population = geraPopulacao(qtd_populacao_inicial, df,ponto_inicial)
population = geraPopulacao(qtd_populacao_inicial, df,ponto_inicial)

#calculo fitness
#Passa a população gerada, o df e a qtd de rotas para a selecão
populacao_qualify, selecao, the_best = calculaFitness(population,df,20) 


while x<qtd_iteraçoes:
    #faz crossover
    selecao_crossover = crossover(selecao,df)
    #calculo fitness
    populacao_qualify, selecao, the_best_out = calculaFitness(selecao_crossover,df,20) 
    x+=1
    x_the_best+=1
    print(f'Fitness = {the_best[0][0]} - Distancia = {the_best[0][1]} | Iterações {x} de {qtd_iteraçoes}')
    #exibo melhor resultado e guardo no the best
    if the_best_out[0][0]>the_best[0][0]:
        the_best[0]=the_best_out[0]
        x=0
        x_the_best=0
        #Escrevendo TXT
        with open('Historico The best.txt', 'a') as file:
            file.write(f'Fitness = {the_best[0][0]} - Distancia = {the_best[0][1]} e Rota = {the_best[0][2]} \n')
        
    








len(populacao_qualify)
len(selecao)  
print(the_best)




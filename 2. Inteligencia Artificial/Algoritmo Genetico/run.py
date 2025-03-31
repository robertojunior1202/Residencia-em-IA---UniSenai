from functions import carregaArquivoTSP, geraPopulacao, calculaFitness

#Implementações Iniciais
caminho="ALL_tsp/att48.tsp/att48.tsp"
skiprows= 6
cabecalho = ["ID", "Latitude", "Longitude"]
qtd_populacao_inicial = 1000
ponto_inicial = 7
the_best = []

#Function importação .TSP
df = carregaArquivoTSP(caminho,skiprows,cabecalho)

#passa a quantidade, o df .tsp e o ponto inicial (opcional)
#population = geraPopulacao(qtd_populacao_inicial, df,ponto_inicial)
population = geraPopulacao(qtd_populacao_inicial, df)

#Passa a população gerada, o df e a qtd de rotas para a selecão
populacao_qualify, selecao, the_best = calculaFitness(population,df,10,the_best) 








len(populacao_qualify)
len(selecao)  
print(the_best)




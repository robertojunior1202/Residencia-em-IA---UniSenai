#Estratégias de Adjacencia
#ea1 - SL-L-NL-N-NO-O-SO-S
#ea2 - S-SL-L-NL-N-NO-O-SO
#ea3 - L-SL-S-NL-N-SO-O-NO
#ea4 - SL-L-S-NL-N-SO-O-NO
#ea5 - SL-L-S-NL-N-SO-NO-O
#ea6 - SL-L-S-NL-N-O-NO-SO

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
        print(f'Estratégia {estrategia} é inválida. Escolha entre ea1 até ea6')

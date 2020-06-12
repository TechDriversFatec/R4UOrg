import api
import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
from collections import Counter
import matplotlib.pyplot as plt
#pip install scikit-fuzzy
#pip install matplotlib

#OS IFS
#Se score_filme for alto e ano_do_filme for alto a recomendação é alta
#Se score_filme for médio e ano_do_filme for alta a recomendação é média
#Se score_filme for baixo e ano_do_filme for alta/média/baixo a recomendação é baixa
#Se score_filme for alta e ano_do_filme for média/baixo a recomendação é média

# variaveis ponto chave
#rank_imdb = ctrl.Antecedent(np.arange(0,100,1),'rank_imdb')
#rank_tomatoes = ctrl.Antecedent(np.arange(0,100,1),'rank_tomatoes')
ano = ctrl.Antecedent(np.arange(1920,2020,1),'ano')
rank = ctrl.Antecedent(np.arange(0,100,1),'rank')
recomendacao = ctrl.Consequent(np.arange(0,100,1),'recomendacao')


#divide por 4 rank
#divisão 2015-2020 novo . 2000 - 2015 medio menor que 2000 velho

rank.automf(names=['pessimo','ruim','medio','bom','otimo'])
recomendacao.automf(names=['muito_baixa','baixa','media','alta','muito_alta'])
ano['atual'] = fuzzy.trimf(ano.universe, [2015,2020,2020])
ano['classico'] = fuzzy.trapmf(ano.universe,[1920,2000,2015,2020])
ano['antigo'] = fuzzy.trimf(ano.universe,[1920,1920,2000])

#grafico matplolib
#ano.view()

#regras Rank e Ano 
rule1 = ctrl.Rule(rank['otimo'] & ano['atual'], recomendacao['muito_alta'])
rule2 = ctrl.Rule(rank['otimo'] & ano['classico'] | rank['bom'] & ano['atual'] | rank['otimo'] & ano['antigo'], recomendacao['alta'])
rule3 = ctrl.Rule(rank['bom'] & ano['classico'] | rank['bom'] & ano['antigo'] | rank['medio'] & ano['classico'] | rank['medio'] & ano['atual'], recomendacao['media'])
rule4 = ctrl.Rule(rank['ruim'] & ano['atual'] | rank['ruim'] & ano['classico'] | rank['medio'] & ano['antigo'], recomendacao['baixa'])
rule5 = ctrl.Rule(rank['pessimo'] & ano['atual'] | rank['pessimo'] & ano['classico'] | rank['pessimo'] & ano['antigo'] | rank['ruim'] & ano['antigo'], recomendacao['muito_baixa'])

recomendacao_crtl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5])
recomendacao_simulacao = ctrl.ControlSystemSimulation(recomendacao_crtl)

def listaFilmesSugestao (filme):
    lista_filmes = {'filme_rep': [], 'rating_rep': [], 'ano_rep': [], 'filme_rat':[], 'ano_rat':[], 'rating_rat':[]}
    #var = api.buscaEssencialFilme(filme)
    #sug_film = rotten_tomatoes.buscaTopsFilmesPorGenero(var['genero'][0]) 
    sug_film = api.filmeSugerido(filme)
    if (len(sug_film['filme_rep'][0]) > 0):
        for filme in range (len(sug_film['filme_rep'][0])):
            dados_filme = api.buscaEssencialFilme(sug_film['filme_rep'][0][filme])
            lista_filmes['ano_rep'].append(dados_filme['ano'])
            media_score = (float(dados_filme['popularidade'][0]) * 10)
            lista_filmes['rating_rep'].append(media_score)
            lista_filmes['filme_rep'].append(sug_film['filme_rep'][0][filme])
    for filme in range (len(sug_film['filme_rat'][0])):
        dados_filme = api.buscaEssencialFilme(sug_film['filme_rat'][0][filme])
        lista_filmes['ano_rat'].append(dados_filme['ano'])
        media_score = (float(dados_filme['popularidade'][0]) * 10)
        lista_filmes['rating_rat'].append(media_score)
        lista_filmes['filme_rat'].append(sug_film['filme_rat'][0][filme])    
    return lista_filmes  

def filtroSugestao (filme):
    filmes_recomendacoes = {'filme_rep':[], 'recomen_rep':[], 'filme_rat':[], 'recomen_rat':[]}
    lista_filmes = listaFilmesSugestao(filme)
    if (len(lista_filmes['filme_rep']) > 0):
        for filme in range (len(lista_filmes['filme_rep'])):
            recomendacao_simulacao.input['rank'] = lista_filmes['rating_rep'][filme]
            recomendacao_simulacao.input['ano'] = lista_filmes['ano_rep'][filme]
            recomendacao_simulacao.compute()
            filmes_recomendacoes['recomen_rep'].append(recomendacao_simulacao.output['recomendacao'])
            filmes_recomendacoes['filme_rep'].append(lista_filmes['filme_rep'][filme])
    for filme in range (len(lista_filmes['filme_rat'])):
        recomendacao_simulacao.input['rank'] = lista_filmes['rating_rat'][filme]
        recomendacao_simulacao.input['ano'] = lista_filmes['ano_rat'][filme]
        recomendacao_simulacao.compute()
        filmes_recomendacoes['recomen_rat'].append(recomendacao_simulacao.output['recomendacao'])
        filmes_recomendacoes['filme_rat'].append(lista_filmes['filme_rat'][filme])
    maior_recomen_rep = max(filmes_recomendacoes['recomen_rep'], key=float)
    posicao_rep = filmes_recomendacoes['recomen_rep'].index(maior_recomen_rep)
    nome_filme_rep = filmes_recomendacoes['filme_rep'][posicao_rep]
    maior_recomen_rat = max(filmes_recomendacoes['recomen_rat'], key=float)
    posicao = filmes_recomendacoes['recomen_rat'].index(maior_recomen_rat)
    nome_filme_rat = filmes_recomendacoes['filme_rat'][posicao]
    return nome_filme_rep, nome_filme_rat

print('\n \nO filme com maior recomendação é : ', filtroSugestao('Les Misérables'))

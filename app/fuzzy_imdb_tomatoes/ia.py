import api
import rotten_tomatoes
import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
#pip install scikit-fuzzy
#pip install matplotlib

#OS IFS
#Se score_filme for alto e ano_do_filme for alto a recomendação é alta
#Se score_filme for médio e ano_do_filme for alta a recomendação é média
#Se score_filme for baixo e ano_do_filme for alta/média/baixo a recomendação é baixa
#Se score_filme for alta e ano_do_filme for média/baixo a recomendação é média

# variaveis ponto chave
rank = ctrl.Antecedent(np.arange(0,100,1),'rank')
ano = ctrl.Antecedent(np.arange(1920,2020,1),'ano')
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

#regras
rule1 = ctrl.Rule(rank['otimo'] & ano['atual'], recomendacao['muito_alta'])
rule2 = ctrl.Rule(rank['otimo'] & ano['classico'] | rank['bom'] & ano['atual'] | rank['otimo'] & ano['antigo'], recomendacao['alta'])
rule3 = ctrl.Rule(rank['bom'] & ano['classico'] | rank['bom'] & ano['antigo'] | rank['medio'] & ano['classico'] | rank['medio'] & ano['atual'], recomendacao['media'])
rule4 = ctrl.Rule(rank['ruim'] & ano['atual'] | rank['ruim'] & ano['classico'] | rank['medio'] & ano['antigo'], recomendacao['baixa'])
rule5 = ctrl.Rule(rank['pessimo'] & ano['atual'] | rank['pessimo'] & ano['classico'] | rank['pessimo'] & ano['antigo'] | rank['ruim'] & ano['antigo'], recomendacao['muito_baixa'])

recomendacao_crtl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5])
recomendacao_simulacao = ctrl.ControlSystemSimulation(recomendacao_crtl)

def filtroSugestao (filme):
    dic_filme = {'filme':[], 'recomendacao':[]}
    if api.buscaFilmeImdb(filme):
        var = api.buscaEssencialFilme(filme)
        sug_film = rotten_tomatoes.buscaTopsFilmesPorGenero(var['genero'][0])   
        cont = 0                    
        for filme in sug_film['filme']:
            print(filme)
            ano_filme = api.buscaEssencialFilme(filme)
            print(ano_filme['ano'])
            print (sug_film['score'][cont])
            recomendacao_simulacao.input['ano'] = ano_filme['ano']
            recomendacao_simulacao.input['rank'] = sug_film['score'][cont]
            recomendacao_simulacao.compute()
            rec = recomendacao_simulacao.output['recomendacao']
            print(rec)
            dic_filme['filme'].append(filme)
            dic_filme['recomendacao'].append(rec)
            cont = cont + 1
        return dic_filme
    else:
        return None

def SugestaoUmFilme (filme):
    var = filtroSugestao(filme)
    cont = 0
    maior_sug = max(var['recomendacao'],key=float)
    for i in var['recomendacao']:
        if maior_sug == i:
            return var['filme'][cont]
        cont = cont + 1

print('\n \nO filme com maior recomendação é : ', SugestaoUmFilme('frozen'))

## biblioteca imdb = pip install IMDbPY
from imdb import IMDb
from collections import Counter

imdb = IMDb()

def buscaImdbGenero ():
    resultado = imdb.search_keyword('romance')
    matrix = ['1970s']
    res = imdb.get_keyword(matrix[0])
    return res

def buscaFilmePorID(x):
    filme = imdb.search_movie(x)
    teste = imdb.get_movie(filme[0].movieID, info='keywords')
    return teste ['keywords']

#print (buscaFilmePorID('frozen'))

#print (buscaImdbGenero())

def buscaEssencialFilme (filme):
    dic = {'elenco':[], 'genero':[],'popularidade':[],'escritor':[],'titulo':[],'ano':[],'tipo':[], 'votos':[], 'keywords':[]}
    a = imdb.search_movie(filme)
    if len(a) != 0:
        try:
            x = imdb.get_movie(a[0].movieID, info=['main'])
            k = imdb.get_movie(a[0].movieID, info=['keywords'])
            dic['elenco'].append(x.get('cast'))
            dic['genero'].append(x.get('genres'))
            dic['popularidade'].append(x.get('rating'))
            dic['escritor'].append(x.get('writer'))
            dic['titulo'].append(x.get('title'))
            dic['ano'].append(x.get('year'))
            dic['votos'].append(x.get('votes'))
            dic['tipo'].append(x.get('kind'))
            dic['keywords'].append(k['keywords'])
        except:
            return None
        return dic

def filmeSugerido (filme):
    lista_filme = {'filme':[], 'rating':[], 'ano':[]}
    dic_filme = {'filme_rep':[], 'rating_rep':[], 'ano_rep':[], 'filme_rat':[], 'rating_rat':[], 'ano_rat': []}
    filme_indicado = buscaEssencialFilme(filme)  
    for index, key in enumerate (filme_indicado['keywords'][0]):
        if index == 5: break
        print('\n',key, '\n')
        for index, filme in enumerate (imdb.get_keyword(key)):
            print(filme)
            if index == 9: break
            fil = buscaEssencialFilme(str(filme))
            if fil != None and fil['tipo'][0] == 'movie' and str(filme_indicado['titulo'][0]) != str(fil['titulo'][0]) and fil['keywords'][0] != None:
                lista_filme['rating'].append(fil['popularidade'])
                lista_filme['filme'].append(fil['titulo'])
                lista_filme['ano'].append(fil['ano']) 
    filme = lista_filme ['filme']
    ano = lista_filme ['ano']
    rating = lista_filme ['rating']
    filme = str(filme).replace('[','').replace(']','').replace("'",'').replace('"','').split(', ')  
    ano = str(ano).replace('[','').replace(']','').replace("'",'').replace('"','').split(', ')
    rating = str(rating).replace('[','').replace(']','').replace("'",'').replace('"','').split(', ')
    dic_filme['filme_rat'].append(filme)
    dic_filme['rating_rat'].append(rating)
    dic_filme['ano_rat'].append(ano)
    counter_filmes = Counter(filme)
    counter_filmes = counter_filmes.most_common()
    list_filmes = []
    for filme in counter_filmes:
        if filme[1] >= 2:
            list_filmes.append(filme[0])
    dic_filme['filme_rep'].append(list_filmes) if len(list_filmes) > 0 else None
    for i in dic_filme['filme_rep'][0]:
        pos = dic_filme['filme_rat'][0].index(i)
        dic_filme['ano_rep'].append(dic_filme['ano_rat'][0][pos])
        dic_filme['rating_rep'].append(dic_filme['rating_rat'][0][pos])
    return dic_filme

#print(filmeSugerido('invocação do mal'))
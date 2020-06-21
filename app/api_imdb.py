# biblioteca imdb = pip install IMDbPY
from imdb import IMDb
from collections import Counter

imdb = IMDb()

def buscaEssencialFilme(filme):
    dic = {'elenco': [], 'genero': [], 'popularidade': [], 'escritor': [],'titulo': [], 'ano': [], 'tipo': [], 'votos': [], 'keywords': []}
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

def listaFilmeSugerido(filme):
    lista_filme = [] 
    dic_filme = {'filme': [], 'rating': [], 'ano': []}
    filme_indicado = buscaEssencialFilme(filme)
    for index, key in enumerate(filme_indicado['keywords'][0]):
        if index == 5: break
        print('\n',index,'-', key, '\n')
        for index, filme in enumerate(imdb.get_keyword(key)):
            print(filme)
            if index == 10: break
            fil = buscaEssencialFilme(str(filme))
            if fil != None and fil['tipo'][0] == 'movie' and str(filme_indicado['titulo'][0]) != str(fil['titulo'][0]) and fil['keywords'][0] != None: lista_filme.append(fil['titulo'][0])
    filme = lista_filme
    filme = str(filme).replace('[', '').replace(']', '').replace("'", '').replace('"', '').split(', ') 
    counter_filmes = Counter(filme)
    counter_filmes = counter_filmes.most_common()
    list_filmes = []
    for filme in counter_filmes:
        if filme[1] >= 2:
            list_filmes.append(filme[0])
    if len(list_filmes) > 0:
        dic_filme['filme'].append(list_filmes)
        for item in dic_filme['filme'][0]:
            var = buscaEssencialFilme(item)
            dic_filme['ano'].append(var['ano'][0])
            dic_filme['rating'].append(var['popularidade'][0])
    else:
        for index, item in enumerate (lista_filme[0]):
            var = buscaEssencialFilme(item)
            dic_filme['filme'].append(item)
            dic_filme['ano'].append(var['ano'][0])
            dic_filme['rating'].append(var['popularidade'][0])
            if len(lista_filme) > 10 and index == 10 or len(lista_filme) == (index + 1): break
    return dic_filme


#print(listaFilmeSugerido('invocação do mal'))

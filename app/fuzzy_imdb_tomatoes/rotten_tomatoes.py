from rotten_tomatoes_client import RottenTomatoesClient, MovieBrowsingQuery, Service, Genre, SortBy, MovieBrowsingCategory

def buscaFilmes(string):
    busca = RottenTomatoesClient.search(term=string,limit=3)
    return busca ['movies']

#print(buscaFilmes('the conjuring'))

def buscaTopsFilmesPorGenero(array):
    dic_filme = {'filme':[],'score':[]}
    query_gen = []
    sci_fan = ['scifi','science-fiction','fantasy', 'sci-fi']
    for nome_genero in array:
        if str(nome_genero).lower() == 'action' or str(nome_genero).lower() == 'adventure':
            #print('passou')
            query_gen.append(Genre.action)
        if str(nome_genero).lower() == 'animation':
            #print('passou')
            query_gen.append(Genre.animation)
        if str(nome_genero).lower() == 'art_and_foreign':
            #print('passou')
            query_gen.append(Genre.art_and_foreign)
        if str(nome_genero).lower() == 'classics':
            #print('passou')
            query_gen.append(Genre.classics)
        if str(nome_genero).lower() == 'comedy':
            #print('passou')
            query_gen.append(Genre.comedy)
        if str(nome_genero).lower() == 'documentary':
            #print('passou')
            query_gen.append(Genre.documentary)
        if str(nome_genero).lower() == 'drama':
            #print('passou')
            query_gen.append(Genre.drama)
        if str(nome_genero).lower() == 'horror':
            #print('passou')
            query_gen.append(Genre.horror)
        if str(nome_genero).lower() == 'kids_and_family' or str(nome_genero).lower() == 'family':
            #print('passou')
            query_gen.append(Genre.kids_and_family)
        if str(nome_genero).lower() == 'mystery' or nome_genero == 'thriller':
            #print('passou')
            query_gen.append(Genre.mystery)
        if str(nome_genero).lower() == 'romance':
            #print('passou')
            query_gen.append(Genre.romance)
        if str(nome_genero).lower() in sci_fan:
            #print('passou')
            query_gen.append(Genre.sci_fi_and_fantasy)    
    query_busca = MovieBrowsingQuery(genres= query_gen, sort_by=SortBy.popularity,services=[Service.netflix, Service.amazon_prime],
                           category=MovieBrowsingCategory.all_dvd_and_streaming)
    resultado = RottenTomatoesClient.browse_movies(query=query_busca)
    #print resultado ['results'][0]
    for i in resultado ['results']:
        dic_filme['filme'].append(i['title'])
        dic_filme['score'].append(i['tomatoScore'])
    return dic_filme

#print (buscaTopsFilmesPorGenero(['action', 'drama']))
# Give me some relatively shitty action, comedy, or romance movies on Netflix or Amazon Prime, sorted by popularity

filmes = MovieBrowsingQuery(minimum_rating=35, maximum_rating=70, services=[Service.netflix, Service.amazon_prime],
                           certified_fresh=False, genres=[Genre.action, Genre.comedy, Genre.romance], sort_by=SortBy.popularity,
                           category=MovieBrowsingCategory.all_dvd_and_streaming)

#print(filmes)
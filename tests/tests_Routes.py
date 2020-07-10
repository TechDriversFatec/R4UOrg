import pytest
import requests

url = 'http://192.168.99.100:5001/'

# os.environ.get('ENV')

# Testes gerais
def teste_filmes_grupo_1():
  response = requests.get(url + 'getFilme/1')
  assert response.status_code == 200

def teste_filmes_grupo_2():
  response = requests.get(url + 'getFilme/2')
  assert response.status_code == 200

def teste_filmes_grupo_3():
  response = requests.get(url + 'getFilme/3')
  assert response.status_code == 200

def teste_filmes_grupo_4():
  response = requests.get(url + 'getFilme/4')
  assert response.status_code == 200

def teste_filmes_grupo_5():
  response = requests.get(url + 'getFilme/5')
  assert response.status_code == 200

def teste_filmes_grupo_6():
  response = requests.get(url + 'getFilme/6')
  assert response.status_code == 200

def teste_filmes_grupo_7():
  response = requests.get(url + 'getFilme/7')
  assert response.status_code == 200

def teste_filmes_grupo_8():
  response = requests.get(url + 'getFilme/8')
  assert response.status_code == 200

def teste_filmes_grupo_9():
  response = requests.get(url + 'getFilme/9')
  assert response.status_code == 200

def teste_erro_string():
  response = requests.get(url + 'getFilme/a')
  assert response.status_code == 400

def teste_erro_numero():
  response = requests.get(url + 'getFilme/10')
  assert response.status_code == 400

def teste_rota_getFilmes():
  response = requests.get(url + 'getFilmes')
  assert response.status_code == 200

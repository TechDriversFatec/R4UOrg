import psycopg2
import json
import pytest

with open('./test_config.json') as fj:
    data = json.load(fj)

con = psycopg2.connect(host='localhost', database='pi', user='fatec', password='fatec')

cur = con.cursor()
cur.execute("CREATE TABLE TEST_FILME AS SELECT * FROM FILME")

xfail = pytest.mark.xfail

def validaCriaFilme(tabela, nome, genero):
    sql = "insert into {} (id ,nome, genero) values (nextval('seq_filme'), '{}','{}')".format(tabela, nome, genero)
    cur.execute(sql)
    con.commit()
    sql = "select * from {} where id = currval('seq_filme')".format(tabela)
    cur.execute(sql)
    recset = cur.fetchall()
    return recset[0][1]

def consulta(tabela):
    sintaxe = 'select * from {}'.format(tabela)
    cur.execute(sintaxe)
    recset = cur.fetchall()
    for rec in recset:
        print (rec)
    con.close()

def consultaFilmeNome():
    sintaxe = "select * from test_filme where nome = 'Joker'"
    cur.execute(sintaxe)
    recset = cur.fetchall()
    return recset[0][1]

def consultaFilmeGenero():
    sintaxe = "select * from test_filme where genero = 'Drama'"
    cur.execute(sintaxe)
    recset = cur.fetchall()
    return recset[0][1]

def test_consultaNome():
    assert consultaFilmeNome() == data['Filme_Valido']
    
def test_validaCriaFilme():
    tabela = 'TEST_FILME'
    nome = 'Joker'
    genero = 'Drama'
    assert validaCriaFilme(tabela, nome, genero) == nome

@xfail
def test_consultaGenero():
    assert consultaFilmeGenero() == data['Genero_Invalido']

@xfail
def test_consultaFilme():
    assert consultaFilmeNome() == data['Filme_Invalido']

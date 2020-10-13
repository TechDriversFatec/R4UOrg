import psycopg2

con = psycopg2.connect(host='localhost', database='pi',
user='fatec', password='fatec')

cur = con.cursor()

#Adicionar o valor das variáveis aqui, até que façamos o teste automatizado real
nome = ''
genero = ''
tabela = ''

def insere(tabela, nome, genero):
    sql = "insert into {} (nome, genero) values ('{}','{}')".format(tabela, nome, genero)
    cur.execute(sql)
    con.commit()
    

def consulta(tabela):
    sintaxe = 'select * from {}'.format(tabela)
    cur.execute(sintaxe)
    recset = cur.fetchall()
    for rec in recset:
        print (rec)
    
def main():
    cur.execute("CREATE TABLE TEST_FILME AS SELECT * FROM FILME")
    consulta(tabela)
    insere(tabela, nome, genero)
    cur.execute("DROP TABLE TEST_FILME")
    con.close()

if __name__ == "__main__":
    main()

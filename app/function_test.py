import psycopg2

con = psycopg2.connect(host='localhost', database='pi',
user='fatec', password='fatec')

cur = con.cursor()

nome = 'Test'
grupo = 5
tabela = 'TEST_FILME'

def insere(nome, genero):
    sql = "insert into TEST_FILME (id, nome, grupo) values (nextval('seq'),'{}','{}')".format(nome, grupo)
    cur.execute(sql)
    con.commit()
    

def consulta(tabela):
    sintaxe = 'select * from {}'.format(tabela)
    cur.execute(sintaxe)
    recset = cur.fetchall()
    for rec in recset:
        print (rec)
    
def main():
    consulta(tabela)
    insere(nome, grupo)
    con.close()

if __name__ == "__main__":
    main()
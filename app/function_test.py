import psycopg2

con = psycopg2.connect(host='', database='',
user='fatec', password='fatec')

cur = con.cursor()

def insere(nome, genero):
    sql = "insert into FILME (nome, genero) values ('{}','{}')".format('nome', 'genero')
    cur.execute(sql)
    con.commit()
    con.close()
    

def consulta(tabela):
    cur.execute('select * from {tabela}').format(tabela)
    recset = cur.fetchall()
    for rec in recset:
        print (rec)
    con.close()
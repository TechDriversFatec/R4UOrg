import psycopg2

con = psycopg2.connect(host='localhost', database='regiao',
user='postgres', password='postgres123')

cur = con.cursor()

nome = ''
genero = ''
tabela = ''

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
    
def main():
    consulta(tabela)
    insere(nome, genero)

if __name__ == "__main__":
    main()
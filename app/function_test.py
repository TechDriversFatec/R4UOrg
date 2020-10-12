import psycopg2

con = psycopg2.connect(host='localhost', database='',
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
    con.close()
    

def consulta(tabela):
    cur.execute('select * from {}').format(tabela)
    recset = cur.fetchall()
    for rec in recset:
        print (rec)
    con.close()
    
def main():
    consulta(tabela)
    insere(tabela, nome, genero)

if __name__ == "__main__":
    main()

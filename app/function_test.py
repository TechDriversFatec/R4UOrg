import psycopg2
import argparse

#python function_test.py -t I -tb Test_Filme -nm Joker -gn Drama
#python function_test.py -t C -tb Test_Filme -nm Sharknado -gn Comedy

#Adicionar o valor das variáveis aqui, até que façamos o teste automatizado real
parser = argparse.ArgumentParser(description='Selecione o teste que deseja fazer: insere / consulta')

parser.add_argument("-t", type = str, 
                    help = "Informe o teste: I / C / CN / CG")

parser.add_argument("-tb", type = str, 
                    help = "Informe o nome da tabela que deseja consultar")

parser.add_argument("-nm", type = str, 
                    help = "Informe o nome do filme")

parser.add_argument("-gn", type = str, 
                    help = "Informe o genero")

args = parser.parse_args()

teste = args.t

tabela = args.tb

nome = args.nm

genero = args.gn

con = psycopg2.connect(host='localhost', database='pi', user='fatec', password='fatec')

cur = con.cursor()

def insere(tabela, nome, genero):
    sql = "insert into {} (id ,nome, genero) values (nextval('seq_filme'), '{}','{}')".format(tabela, nome, genero)
    cur.execute(sql)
    con.commit()
    

def consulta(tabela):
    sintaxe = 'select * from {}'.format(tabela)
    cur.execute(sintaxe)
    recset = cur.fetchall()
    for rec in recset:
        print (rec)
    
def consultaFilmeNome(tabela, nome):
    sintaxe = "select * from {} where nome = '{}'".format(tabela, nome)
    cur.execute(sintaxe)
    recset = cur.fetchall()
    for rec in recset:
        print (rec)

def consultaFilmeGenero(tabela, genero):
    sintaxe = "select * from {} where genero = '{}'".format(tabela, genero)
    cur.execute(sintaxe)
    recset = cur.fetchall()
    for rec in recset:
        print (rec)

def main():
    #cur.execute("CREATE TABLE TEST_FILME AS SELECT * FROM FILME")
    if (teste == 'I'):
        insere(tabela, nome, genero)
    elif (teste == 'C'):
        consulta(tabela)
    elif (teste == 'CN'):
        consultaFilmeNome(tabela, nome)
    elif (teste == 'CG'):
        consultaFilmeGenero(tabela, genero)
    else:
        print('Valor selecionado inválido!')
    #cur.execute("DROP TABLE TEST_FILME")
    con.close()

if __name__ == "__main__":
    main()

import psycopg2
import argparse

#python function_test.py -t I -tb Filme -nm Joker -gn Drama
#python function_test.py -t C -tb Filme -nm Sharknado -gn Comedy


#Adicionar o valor das variáveis aqui, até que façamos o teste automatizado real
parser = argparse.ArgumentParser(description='Selecione o teste que deseja fazer: insere / consulta')

parser.add_argument("-t", type = str, 
                    help = "Informe o teste: I / C ")

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


con = psycopg2.connect(host='localhost', database='',
user='fatec', password='fatec')

cur = con.cursor()

def insere(tabela, nome, genero):
    sql = "insert into {} (nome, genero) values ('{}','{}')".format(tabela, nome, genero)
    cur.execute(sql)
    con.commit()
    con.close()
    

def consulta(tabela):
    sintaxe = 'select * from {}'.format(tabela)
    cur.execute(sintaxe)
    recset = cur.fetchall()
    for rec in recset:
        print (rec)
    con.close()
    
def main():
    if (teste == 'I'):
        insere(tabela, nome, genero)
    elif (teste == 'C'):
        consulta(tabela)
    else:
        print('Valor selecionado inválido')


if __name__ == "__main__":
    main()

import random
from conexaoBancoDados import *
import sys
from leitorCodigoBarras import *

# conexão com o banco de dados
connection = create_server_connection("localhost", "root", "banco2018")
execute_query(connection, """USE codigo""")

print('\nDeseja criar um código de barras aleatório ou inserir um código de barras com 12 digitos?\n')

opcao = input(
    '1 - Criar código de barra aleatório\n2 - Inserir um código de barra\n3 - Leia um código de barra\n\n')


if opcao == '1':

    codigoBarras = random.randint(1000000000000, 9999999999999)


elif opcao == '2':

    codigoBarras = input('Digite o código de barras: ')

    if len(codigoBarras) != 12 or codigoBarras.isdigit() == False:
        print('\nCódigo de Barras inválido, por favor tente novamente inserindo um código válido com 12 números!')
        sys.exit()

elif opcao == '3':
    produto = input('Digite o nome da imagem para ler o código de barra: ')
    lerCodigo(produto)
    sys.exit()

else:
    print('\nOpção inválida, por favor tente novamente!')
    sys.exit()


nomeProduto = input("\nDigite o nome do produto: \n")
codigoBarras = str(codigoBarras)

query = "INSERT INTO CodigoBarra (codigo , nome) VALUES (%s,%s);"
dados = (codigoBarras, nomeProduto)

execute_query_data(connection, query, dados)

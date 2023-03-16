import mysql.connector
from mysql.connector import Error
from barcode import EAN13
from barcode.writer import ImageWriter

# função que cria a conexão com o banco de dados


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database conectado com sucesso!")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# função que criar o banco dados


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Banco de dados criado com sucesso!")
    except Error as err:
        print(f"Error: '{err}'")

# função que executa a query sem os dados


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Execução de Query feita com Sucesso!")
    except Error as err:
        print(f"Error: '{err}'")

# função que executa a query com dados


def execute_query_data(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()

        # criação da imagem do código de barras
        codigoBarrasImagem = EAN13(str(data[0]), writer=ImageWriter())
        codigoBarrasImagem.save('produtos/' + data[1].lower())

        print('\nO código de barra do produto ' + data[1] +
              ' foi criado com sucesso com a numeração: ' + str(codigoBarrasImagem))

    except Error as err:
        print(f"Error: '{err}'")
        print('\nCódigo de barras já existe!')

# função que retorna a consulta da query


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


# connection = create_server_connection("localhost", "root", "banco2018")
# execute_query(connection, """USE codigo""")

# q1 = """
# SELECT * FROM CodigoBarra;
# """
# results = read_query(connection, q1)

# print(results)


# criarBancoDadosQuery = "CREATE DATABASE codigo"
# create_database(connection, criarBancoDadosQuery)

# criarTabelaCodigoBarra = """
#  CREATE TABLE CodigoBarra (
#    codigo VARCHAR(13) PRIMARY KEY,
#    nome VARCHAR(60) NOT NULL
#    );
#   """


# execute_query(connection, criarTabelaCodigoBarra)

import mysql.connector
from mysql.connector import Error

def criar_banco():
  conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
  )
  cursor = conexao.cursor()

  cursor.execute("""
    SELECT SCHEMA_NAME 
        FROM information_schema.SCHEMATA 
        WHERE SCHEMA_NAME = 'gestaodesaude'
  """)

  existe = cursor.fetchone()

  if not existe:
   cursor.execute(
     "CREATE DATABASE gestaodesaude DEFAULT CHARACTER SET utf8"
   )
   print("banco de dados criado com sucesso")
  else:
    print("Conectado ao banco")

  cursor.close()
  conexao.close()
# def conectar():
def conectar():
  try:
   return mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "",
     database = "gestaodesaude"
     )
  except Error as e:
    print("Erro ao conectar ao mysql: ",e)
    return None
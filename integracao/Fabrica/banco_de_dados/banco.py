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
      WHERE SCHEMA_NAME = 'fabrica'
  """)
  existe = cursor.fetchone()

  if not existe:
    cursor.execute(
      "CREATE DATABASE fabrica DEFAULT CHARACTER SET utf8"
    )
    print("banco de dados criado com sucesso!")
  else:
    print("Banco de dados já existe, não precisa ser criado")

  cursor.close()
  conexao.close()

def conectar():
  try:
    return mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "",
      database = "fabrica"
    )
  except Error as e:
    print("Erro ao conectar ao banco:", e)
    return None
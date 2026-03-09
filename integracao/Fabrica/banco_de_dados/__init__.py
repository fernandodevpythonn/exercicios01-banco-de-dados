from .banco import criar_banco, conectar
from .tabelas import criar_tabela 
def inicializar_sistema():
  criar_banco()
  conexao = conectar()
  if conexao is not None:
    cursor = conexao.cursor()
    criar_tabela(cursor)
    cursor.close()
    conexao.close()
inicializar_sistema()
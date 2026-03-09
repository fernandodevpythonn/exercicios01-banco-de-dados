from .banco import criar_banco,conectar
from .tabela import criar_tabela
def iniciar_sistema():
  criar_banco()
  conexao = conectar()
  if conexao:
    cursor = conexao.cursor()
    criar_tabela(cursor)
    conexao.commit()
    conexao.close()
    cursor.close()
iniciar_sistema()
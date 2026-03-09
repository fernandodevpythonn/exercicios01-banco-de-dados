from banco_de_dados import iniciar_sistema,conectar
from banco_de_dados.tabela import *
from datetime import date
iniciar_sistema()

def menu():
   print("==MENU==")
   print("1 - Cadastrar paciente")
   print("2 - cadastrar especialidade")
   print("3 - cadastrar médico")
   print("4 - cadastrar consulta")
   print("5 - cadastrar relação de médicos e especialidades")
def main():
   
    while True:
      menu()
      opcao = input("Escolha uma opção:")

      conexao = conectar()
      cursor = conexao.cursor()

      match opcao:
        case "1":
          cadastrar_paciente(cursor,
                              input("nome: "),
                              int(input("cpf: ")),
                              input("email: "))
          conexao.commit()
          print("paciente cadastrado")
        case "2":
          cadastrar_especialidade(cursor,
                                   input("nome: "),
                                  int(input("id médico: ")))
          conexao.commit()
          print("especialidade cadastrada")
        case "3":
          cadastrar_medico(cursor,
                             input("nome: "),
                             input("especialidade: "))
          conexao.commit()
          print("médico cadastrado")
        case "4":
          cadastrar_consulta(cursor,
                               int(input("id do paciente: ")),
                               date.fromisoformat(input("horário: ")),
                               int(input("id do médico: ")))
          conexao.commit()
          print("consulta cadastrada")
        case "5":
          cadastrar_medico_especialidade(cursor,
                                         int(input("id do médico: ")),
                                         int(input("id da especialidade: ")))
          conexao.commit()
          print("relacionado com sucesso")

if __name__ == "__main__":
  main()
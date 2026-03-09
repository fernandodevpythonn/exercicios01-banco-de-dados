from banco_de_dados import criar_banco,conectar
from datetime import date
def criar_tabela(cursor):
  cursor.execute("""
     CREATE TABLE IF NOT EXISTS paciente(
        idpaciente INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(45) NOT NULL,
        cpf INT NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE
     )
  """)
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS medico(
       idmedico INT AUTO_INCREMENT PRIMARY KEY,
       nome VARCHAR(50) NOT NULL,
       especialidade VARCHAR(45) NOT NULL
      )
  """)
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS especialidade(
        idespecialidade INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(45) NOT NULL,
        medico_idmedico INT NOT NULL,
        FOREIGN KEY (medico_idmedico) REFERENCES medico(idmedico)
      )    
  """)
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS consulta(
        idconsulta INT AUTO_INCREMENT PRIMARY KEY,
        horario DATETIME NOT NULL,
        medico_idmedico INT NOT NULL,
        paciente_idpaciente INT NOT NULL,
        FOREIGN KEY (medico_idmedico) REFERENCES medico(idmedico),
        FOREIGN KEY (paciente_idpaciente) REFERENCES paciente(idpaciente)
      )
  """)
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS medico_especialidades(
       medico_idmedico INT NOT NULL,
       especialidade_idespecialidade INT NOT NULL,
       PRIMARY KEY (medico_idmedico, especialidade_idespecialidade),
       FOREIGN KEY (medico_idmedico) REFERENCES medico(idmedico),
       FOREIGN KEY (especialidade_idespecialidade) REFERENCES especialidade(idespecialidade)
      ) ENGINE=innoDB;
  """)



def cadastrar_paciente(cursor,nome,cpf,email):
    cursor.execute("""
       INSERT INTO paciente (nome,cpf,email)
       VALUES (%s,%s,%s)
    """, (nome,cpf,email))

def cadastrar_especialidade(cursor,nome,medico_idmedico):
    cursor.execute("""
     INSERT INTO especialidade (nome,medico_idmedico)
     VALUES (%s,%s)
    """, (nome,medico_idmedico))

def cadastrar_medico(cursor,nome,especialidade):
    cursor.execute("""
      INSERT INTO medico (nome,especialidade)
      VALUES (%s,%s)
    """,(nome,especialidade))
def cadastrar_consulta(cursor,paciente_idpaciente,horario,medico_idmedico):
    cursor.execute("""
      INSERT INTO consulta (paciente_idpaciente,horario,medico_idmedico)
      VALUES (%s,%s,%s)
    """, (paciente_idpaciente,date(2026, 3, 10),medico_idmedico))
def cadastrar_medico_especialidade(cursor,medico_idmedico,especialidade_idespecialidade):
    cursor.execute("""
      INSERT INTO medico_especialidades (medico_idmedico,especialidade_idespecialidade)
      VALUES (%s,%s)
    """, (medico_idmedico,especialidade_idespecialidade))
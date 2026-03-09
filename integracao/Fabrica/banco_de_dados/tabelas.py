
def criar_tabela(cursor):
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS fornecedor(
          idfornecedor INT AUTO_INCREMENT PRIMARY KEY,
          nome VARCHAR(45) NOT NULL
          )
  """)
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS material(
          idmaterial INT AUTO_INCREMENT PRIMARY KEY,
          nome VARCHAR(45) NOT NULL,
          )
  """)
  cursor.execute("""
     CREATE TABLE IF NOT EXISTS ordem_de_producao(
        idordem_de_producao INT AUTO_INCREMENT PRIMARY KEY,
        ordem VARCHAR(45) NOT NULL,
        FOREIGN KEY(material_idmaterial) REFERENCES material(idmaterial)
        )
""")
  cursor.execute("""
     CREATE TABLE IF NOT EXISTS funcionario(
                 idfuncionario INT AUTO_INCREMENT PRIMARY KEY,
                 nome VARCHAR(45) NOT NULL
                 )
  """)
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS produto(
                 idproduto INT AUTO_INCREMENT PROMARY KEY,
                 nome VARCHAR(45) NOT NULL,
                 valor FLOAT NOT NULL,
                 marca VARCHAR(45) NOT NULL,
                 )
""")
  
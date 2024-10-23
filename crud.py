from sqlalchemy.orm import Session
import models, schemas

# Função para criar uma nova pessoa no banco de dados
# Parâmetros:
#    - db: sessão do banco de dados (Session)
#    - pessoa: objeto contendo os dados da pessoa a ser criada (schemas.PessoaCreate)
def create_pessoa(db: Session, pessoa: schemas.PessoaCreate):
    db_pessoa = models.Pessoa(**pessoa.model_dump()) # Cria um novo objeto 'Pessoa' utilizando os dados fornecidos e convertidos em dicionário
    db.add(db_pessoa)  # Adiciona a nova pessoa à sessão do banco de dados
    db.commit()  # Confirma as mudanças no banco de dados
    db.refresh(db_pessoa)  # Atualiza o objeto 'db_pessoa' com os dados mais recentes do banco
    return db_pessoa  # Retorna a pessoa criada

# Função para listar todas as pessoas do banco de dados
def get_pessoas(db: Session, skip: int = 0):
    return db.query(models.Pessoa).offset(skip).all() # Consulta todas as pessoas do banco e retorna a lista

# Função para obter uma pessoa específica pelo ID
def get_pessoa(db: Session, pessoa_id: int):
    return db.query(models.Pessoa).filter(models.Pessoa.id == pessoa_id).first() # Consulta o banco e retorna a primeira pessoa com o ID correspondente

# Função para atualizar uma pessoa existente no banco de dados
def update_pessoa(db: Session, pessoa_id: int, pessoa_data: schemas.PessoaCreate):
    pessoa = db.query(models.Pessoa).filter(models.Pessoa.id == pessoa_id).first()
    if pessoa:
        # Se a pessoa for encontrada, itera sobre os dados fornecidos e atualiza os atributos da pessoa
        for key, value in pessoa_data.model_dump().items():
            setattr(pessoa, key, value) # Atualiza o atributo correspondente com o novo valor
        db.commit()
        db.refresh(pessoa)
        return pessoa
    return None # Retorna None se a pessoa não for encontrada

# Função para deletar uma pessoa do banco de dados
def delete_pessoa(db: Session, pessoa_id: int):
    pessoa = db.query(models.Pessoa).filter(models.Pessoa.id == pessoa_id).first()
    if pessoa:
        db.delete(pessoa)  # Deleta a pessoa do banco de dados
        db.commit()
        return pessoa
    return None

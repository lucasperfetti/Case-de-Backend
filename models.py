from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

# Base para criar os modelos do SQLAlchemy, vinculando as classes às tabelas do banco de dados
Base = declarative_base()

# Modelo que representa a tabela 'pessoas' no banco de dados
class Pessoa(Base):
    __tablename__ = "pessoas" # Nome da tabela no banco de dados
    
    # -- Definição das colunas da tabela --
    id = Column(Integer, primary_key=True, index=True) # 'id' é a chave primária, com um índice para melhorar a eficiência nas buscas
    nome_completo = Column(String, index=True)
    data_nascimento = Column(Date)
    endereco = Column(String)
    cpf = Column(String, unique=True, index=True)
    estado_civil = Column(String)

    # Método para converter os atributos da instância da classe 'Pessoa' em um dicionário
    def to_dict(self):
        return {
            "id": self.id,
            "nome_completo": self.nome_completo,
            "data_nascimento": self.data_nascimento.isoformat() if self.data_nascimento else None,
            "endereco": self.endereco,
            "cpf": self.cpf,
            "estado_civil": self.estado_civil,
        }

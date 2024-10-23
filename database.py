from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão para o banco de dados SQLite
# O banco de dados será armazenado localmente no arquivo 'pessoas.db' na raiz do projeto
SQLALCHEMY_DATABASE_URL = "sqlite:///./pessoas.db"

# Cria a engine que fará a conexão com o banco de dados SQLite
# O parâmetro 'check_same_thread' é necessário no SQLite para permitir que a mesma conexão seja usada em diferentes threads
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Cria uma fábrica de sessões (SessionLocal) que será usada para interagir com o banco de dados
# As sessões criadas não realizarão commit ou flush automáticos, isso deve ser feito manualmente no código
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base será usada para criar as classes de modelo que representam as tabelas no banco de dados
Base = declarative_base()

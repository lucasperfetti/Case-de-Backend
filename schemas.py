from pydantic import BaseModel, StringConstraints
from typing import Annotated
from datetime import date

# Esquema base para a entidade Pessoa, define os atributos principais
class PessoaBase(BaseModel):
    # Strings com validação 'StringConstraints', que remove espaços e exige que não seja nulo
    nome_completo: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1)
    ]
    data_nascimento: date
    endereco: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1)
    ]
    # 'cpf': string validada com pattern para garantir que possui exatamente 11 dígitos
    cpf: Annotated[
        str,
        StringConstraints(min_length=11, max_length=11, pattern=r"^\d{11}$")
    ]
    estado_civil: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1)
    ]

# Esquema para criação de uma nova Pessoa, herda os atributos de PessoaBase
class PessoaCreate(PessoaBase):
    pass # Não adiciona novos atributos, reutiliza o esquema base

# Esquema para representação de uma Pessoa já cadastrada no banco de dados, incluindo o 'id'
class Pessoa(PessoaBase):
    id: int

# Configuração do modelo que ativa o suporte a ORM para permitir a conversão de objetos SQLAlchemy
model_config = {
        'from_attributes': True  # Ativa o suporte a ORM para permitir conversão direta de objetos do banco para os esquemas
    }

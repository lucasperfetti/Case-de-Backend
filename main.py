from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import models, crud, schemas
from database import SessionLocal, engine

# Criar as tabelas no banco de dados
# models.Base.metadata.create_all(bind=engine) cria as tabelas definidas no models.py no banco de dados.
models.Base.metadata.create_all(bind=engine)

# Instância da aplicação FastAPI
app = FastAPI()

# Dependência para obter a sessão do banco de dados
# Esta função `get_db` é utilizada nas rotas para abrir e fechar uma conexão com o banco de dados automaticamente.
def get_db():
    db = SessionLocal() # Cria uma nova sessão de banco de dados
    try:
        yield db # Retorna a sessão para ser usada na função chamadora
    finally:
        db.close() # Fecha a sessão após o uso

# Rota POST para criar uma nova pessoa
@app.post("/pessoas/", response_model=schemas.Pessoa)
def create_pessoa(pessoa: schemas.PessoaCreate, db: Session = Depends(get_db)):
    nova_pessoa = crud.create_pessoa(db=db, pessoa=pessoa) # Cria uma nova pessoa no banco de dados.
    return JSONResponse(
        status_code=201,  # HTTP 201 Created
        content={"message": "Pessoa criada com sucesso!", "data": nova_pessoa.to_dict()} 
    )

# Rota GET para listar todas as pessoas
@app.get("/pessoas/", response_model=list[schemas.Pessoa])
def get_pessoas(skip: int = 0, db: Session = Depends(get_db)): # `skip` define o número de entradas a serem ignoradas.
    pessoas = crud.get_pessoas(db, skip=skip) # Chama a função CRUD para obter as pessoas.
    if not pessoas:
        return JSONResponse(
            status_code=404,  # HTTP 404 Not Found
            content={"msg": "Nenhuma pessoa encontrada."}
        )
    return JSONResponse(
        status_code=200,  # HTTP 200 OK
        content={"msg": "Lista de pessoas", "data": [pessoa.to_dict() for pessoa in pessoas]} # Retorna uma lista de pessoas no banco de dados.
    )

# Rota GET para obter uma pessoa específica por ID
@app.get("/pessoas/{pessoa_id}", response_model=schemas.Pessoa)
def get_pessoa(pessoa_id: int, db: Session = Depends(get_db)):
    db_pessoa = crud.get_pessoa(db, pessoa_id=pessoa_id) # Chama a função CRUD para obter a pessoa pelo ID.
    if db_pessoa is None:
        return JSONResponse(
            status_code=404,  # HTTP 404 Not Found
            content={"msg": "Pessoa não encontrada."}
        )
    return JSONResponse(
        status_code=200,  # HTTP 200 OK
        content={"msg": "Pessoa encontrada!", "data": db_pessoa.to_dict()}  # Retorna os dados de uma pessoa específica a partir de seu ID.
    )

# Rota PUT para atualizar uma pessoa existente
@app.put("/pessoas/{pessoa_id}", response_model=schemas.Pessoa)
def update_pessoa(pessoa_id: int, pessoa: schemas.PessoaCreate, db: Session = Depends(get_db)):
    pessoa_atualizada = crud.update_pessoa(db=db, pessoa_id=pessoa_id, pessoa_data=pessoa) # Atualiza os dados da pessoa através do id.
    if pessoa_atualizada is None:
        return JSONResponse(
            status_code=404,  # HTTP 404 Not Found
            content={"msg": "Pessoa não encontrada."}
        )
    return JSONResponse(
        status_code=200,  # HTTP 200 OK
        content={"msg": "Pessoa atualizada com sucesso!", "data": pessoa_atualizada.to_dict()} # Retorna os dados atualizados.
    )

# Rota DELETE para excluir uma pessoa
@app.delete("/pessoas/{pessoa_id}")
def delete_pessoa(pessoa_id: int, db: Session = Depends(get_db)):
    pessoa_excluida = crud.delete_pessoa(db=db, pessoa_id=pessoa_id) # Exclui a pessoa pelo ID
    if pessoa_excluida is None:
        return JSONResponse(
            status_code=404,  # HTTP 404 Not Found
            content={"msg": "Pessoa não encontrada."}
        )
    return JSONResponse(
        status_code=200,  # HTTP 200 OK
        content={"msg": "Pessoa deletada com sucesso!"}
    )

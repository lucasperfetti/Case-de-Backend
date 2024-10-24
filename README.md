# Case-de-Backend
API desenvolvida em FastAPI para realizar operações CRUD de cadastro e gestão de pessoas, utilizando banco de dados SQLite. A API inclui funcionalidades como criação, leitura, atualização e exclusão de registros de pessoas.

## Pré-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório
```bash
git clone https://github.com/lucasperfetti/Case-de-Backend.git
cd Case-de-Backend
```
2. Criando um ambiente virtual para o projeto
```bash
# Para Windows
py -m venv venv

# Para macOS e Linux
python3 -m venv venv
```

3. Ativando o ambiente virutal
```bash
# Para Windows
.\venv\Scripts\activate

# Para macOS e Linux
source venv/bin/activate
```

4. Instalando as dependências
```bash
pip install -r requirements.txt
```

5. Executando a API
```bash
uvicorn main:app --reload
```

6. Acessando a documentação
```bash
http://127.0.0.1:8000/docs
```

Interface para operações de CRUD
v![image](https://github.com/user-attachments/assets/7efbeb76-e37e-4b4d-9af2-04ab3c6f8559)

# API REST - Football Data

## Descrição
A API REST desenvolvida para armazenar e fornecer dados de jogadores e clubes de futebol.

## Estrutura do Projeto
* `app.py`: Arquivo principal da aplicação, contendo a lógica da API REST
* `DB/`: Diretório que contém o banco de dados SQLite `futebol.db`
* `README.md`: Este arquivo, contendo informações sobre o projeto
* `Requeriments.txt`: Arquivo que lista as dependências necessárias para o projeto

## Estrutura do Banco de Dados

O banco de dados SQLite `futebol.db` possui as seguintes tabelas:

### Tabela `clube`
- **id** (INTEGER, PRIMARY KEY, AUTOINCREMENT): Identificador único do clube.
- **nome** (STRING, NOT NULL): Nome do clube.
- **localizacao** (STRING): Localização do clube.

### Tabela `jogador`
- **id** (INTEGER, PRIMARY KEY, AUTOINCREMENT): Identificador único do jogador.
- **nome** (STRING, NOT NULL): Nome do jogador.
- **idade** (INTEGER): Idade do jogador.
- **posicao** (STRING): Posição do jogador no campo.
- **clube_id** (INTEGER, FOREIGN KEY): Identificador do clube ao qual o jogador pertence. Referência para a tabela `clube`.


## Funcionalidades
* Armazena dados de jogadores e clubes de futebol
* Fornece uma API REST para inserir e ler dados externamente
* Suporta operações de leitura e criação de clubes e jogadores

## Requisitos de Instalação
* Banco de dados SQLite (futebol.db)
* Linguagem de programação: Python
* Framework: Flask
* Bibliotecas necessárias: Flask-SQLAlchemy
* IDE: Visual Studio Code
* Extensão do Visual Studio Code : SQLite Viewer (para visualizar e gerenciar o banco de dados SQLite)
* API REST local em execução no endereço `http://localhost:5000`

## Instalação das Dependências
 Execute o comando `pip install -r requeriments.txt` para instalar as dependências necessárias para o projeto.
 
 ## Ferramentas Recomendadas
* IDE: Visual Studio Code
* Extensão do Visual Studio Code : SQLite Viewer (para visualizar e gerenciar o banco de dados SQLite)


## Uso
* Execute o comando `python app.py` para iniciar a API
* Use a API para inserir e ler dados de jogadores e clubes de futebol
* Endpoints disponíveis:
	+ `GET /clubes`: Retorna uma lista de clubes
	+ `GET /jogadores`: Retorna uma lista de jogadores
	+  `POST /clube`: Cria um novo clube. Exemplo de corpo da requisição:
    ```json
    {
      "nome": "Nome do Clube",
      "localizacao": "Localização do Clube"
    }
    ```
  - `POST /jogador`: Cria um novo jogador. Exemplo de corpo da requisição:
    ```json
    {
      "nome": "Nome do Jogador",
      "idade": 25,
      "posicao": "Atacante",
      "clube_id": 1
    }
    ```

## Desenvolvedor
Desenvolvido por **Guilherme Neto**	

# API de Conta Bancária

Este projeto implementa uma API simples de Conta Bancária usando Python e Flask. Ele fornece funcionalidades para registro de usuário, login com autenticação JWT e gerenciamento de saldos de contas bancárias.

## Funcionalidades

- **Registro de Usuário**: Permite que novos usuários criem uma conta.
- **Login de Usuário**: Autentica usuários e emite JSON Web Tokens (JWT) para acesso seguro.
- **Gerenciamento de Saldo**: Permite que usuários autenticados atualizem o saldo de suas contas bancárias.

## Tecnologias Utilizadas

- **Python**: A linguagem de programação principal.
- **Flask**: Um micro framework web para Python, usado para construir a API.
- **JWT (JSON Web Tokens)**: Usado para autenticação e autorização seguras.
- **SQLite**: Um banco de dados leve baseado em arquivo, usado para persistência de dados (`storage.db`).

## Como Rodar Localmente

Siga estes passos para configurar e rodar o projeto em sua máquina local:

1.  **Clonar o Repositório**:

    ```bash
    git clone https://github.com/thiagonmiziara/jwt.git
    cd jwt
    ```

2.  **Criar um Ambiente Virtual** (recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  **Instalar Dependências**:

    ```bash
    pip install -r requirements.txt
    ```

    _(Nota: Se `requirements.txt` não existir, você pode criá-lo executando `pip freeze > requirements.txt` após instalar os pacotes necessários como Flask, PyJWT, etc.)_

4.  **Inicializar o Banco de Dados**:
    O projeto usa um banco de dados SQLite. Você precisa inicializar o esquema.

    ```bash
    sqlite3 storage.db < init/schema.sql
    ```

5.  **Iniciar o Servidor Flask**:
    ```bash
    python run.py
    ```
    A API estará rodando em `http://0.0.0.0:5000` (ou `http://localhost:5000`).

## Estrutura do Projeto

O projeto segue uma abordagem estruturada para organizar seus componentes:

- `run.py`: O ponto de entrada da aplicação.
- `storage.db`: O arquivo do banco de dados SQLite.
- `init/`: Contém scripts de inicialização do banco de dados.
  - `schema.sql`: Script SQL para criar tabelas do banco de dados.
- `src/`: Contém o código-fonte principal.
  - `configs/`: Arquivos de configuração (ex: configurações JWT).
  - `controllers/`: Lógica de negócios e manipuladores para operações específicas.
  - `drivers/`: Implementações para serviços externos (ex: manipulação de JWT, hash de senha).
  - `errors/`: Tratamento de erros personalizados e tipos de exceção.
  - `main/`: Configuração principal da aplicação.
    - `composer/`: Compõe controladores e dependências.
    - `middlewares/`: Middleware para processamento de requisições (ex: autenticação JWT).
    - `routes/`: Define os endpoints da API.
    - `server/`: Instância da aplicação Flask e configuração do servidor.
  - `models/`: Modelos de banco de dados e repositórios para interação com dados.
  - `views/`: Lida com requisições e respostas HTTP, e define interfaces para as views.

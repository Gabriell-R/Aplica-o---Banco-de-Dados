# Trabalho Prático de Banco de Dados - CRUD

Este é o projeto da aplicação (Parte 3) da disciplina de Banco de Dados. O sistema foi feito em Python e executa as operações de CRUD (Create, Read, Update e Delete) para as tabelas Clube, Jogador e Contrato.

# Bibliotecas necessárias

Para rodar o código, é preciso instalar o Flask e o conector do MySQL. No terminal, execute:

pip install Flask
pip install mysql-connector-python

# Banco de Dados

O banco de dados utilizado é o `atividade3bd`. O script com a criação das tabelas está no arquivo `Atividade3BD.sql` dentro da pasta `sql`. Basta rodar esse script no seu gerenciador do MySQL.

# Como rodar a aplicação

1. Abra o arquivo `app.py`.
2. Na função `conectar_banco()`, insira a senha do seu usuário do MySQL.
3. Execute o arquivo `app.py` no terminal.
4. Abra o navegador e acesse: http://127.0.0.1:5000

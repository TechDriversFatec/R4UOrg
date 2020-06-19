## Tópicos Avançados em Banco de Dados

Projeto de inteligência artificial, para interação com a assistente virtual do primeiro semestre.

- [x] IA - lógica Fuzzy
- [x] Elaboração e distribuição da planilha para obtenção de dados - Dados para treinamento IA
- [x] Disponibilizar acesso da aplicação no Heroku
- [x] Rotas para acesso do assistente à aplicação
- [x] Banco e modelagem

### Primeira entrega

- Levantamento de requisitos, planejamento das sprints e organização de tasks no trello.
- Configuração do ambiente de desenvolvimento docker com python, postgres e bibliotecas de python.
- Criação de tabelas, relacionamentos e modelagem.
- Preparação de scripts sql para inserção no banco, tanto inglês quanto em português.
- Estudo das bibliotecas IMDB e JustWatch.
- Estudo para criação de rota inicial e conexão com o banco.

### Segunda entrega

- Implementação da conexão com banco.
- Criação dos models de gênero e usuário.
- Criação das rotas iniciais para cadastro de gênero atrelado à um grupo.
- Implementação inicial da busca dos dados da IMDB.

### Terceira entrega

- Rota de exemplo para disponibilizar ao primeiro semestre.
- PoC da funcionalidade do IA com a interação dos dados analisados pelas bibliotecas _IMDB_ e _RottenTomatoes_.
- Pesquisa e aplicação da biblioteca _Scikit-Fuzzy_ para desenvolvimento IA.
- Desenvolvimento e conexão com banco.

### Quarta entrega

- Rotas já fazendo a comunicação com o banco do Docker.
- Filtro com base nos dados do banco, de forma que as recomendações da IA façam sentido.
- Coleta de dados (planilha de filmes favoritos de todos os alunos envolvidos no PI).

### Quinta entrega

- Como fazer a instalação do projeto

  - Ter o Python instalado na sua máquina
  - Instalar um editor de texto da sua preferência (indicamos VSCode ou Pycharm)
  - Instalar o Docker desktop na sua máquina (há versões para Windows, Linux e Mac)
  - Fazer o clone do projeto em algum diretório da sua preferência
  - Entrar na pasta raiz do projeto através do comando "cd Topicos_Avancados"
  - Na pasta raiz executar o comando "docker-compose up -d"
  - Acessar a rota http://locahost:5001/getFilme/(algum número de 1 a 9)
  - Os números de 1 a 9 são os números de cada grupo que participa do projeto Integrador

- Links úteis:
  - Python: https://www.python.org/
  - Docker: https://www.docker.com/
  - VSCode: https://code.visualstudio.com/
  - JetBrains: https://www.jetbrains.com/pt-br/pycharm/

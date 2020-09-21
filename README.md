## Tópicos Avançados em Banco de Dados

- Introdução do projeto

  - Nosso projeto consiste numa API que se utiliza Inteligência Artificial para fazer interações com uma base de dados preexistente.

- Objetivos

  - O objetivo central do projeto é fazer recomendações inteligentes de filmes baseado no perfil individual de cada usuário.

- Tecnologias utilizadas

  - Python - Escolhemos trabalhar com a linguagem de programação Python devido à sua grande popularidade em sistemas que utilizam Inteligência Artificial. Um outro motivo para a escolha do Python foi visando uma maior integração com os alunos do primeiro semestre, uma vez que muitos deles estão tendo contato com a programação pela primeira vez e isso ajudaria a dar um melhor suporte para eventuais dúvidas.
  - Flask - Várias funcionalidades úteis na aplicação com Python, sendo a principal delas as rotas de acesso.
  - Fuzzy - Biblioteca de Inteligência Artificial que permitiu fazer as análises e recomendações.
  - Postgresql - Banco de dados relacional que guarda a massa de filmes.
  - SQLAlchemy - Comunicação do Python com o Postgresql.
  - Docker - Foi utilizado visando eliminar qualquer problema de incompatibilidade entre os membros da equipe, pois o projeto fica exatamente igual para todos independentemente de onde ele é acessado.
  - Heroku - Utilizado para hospedar e disponibilizar a API online para os alunos.
  - Sistemas de versionamento de código - Git e Github para uma melhor integração e organização dos códigos da disciplina.
  - Trello - Organização e controle de tasks pelo Scrum Master e PO e acesso claro de prazos e requisitos pelos outros membros da equipe.
  - Pytest - Biblioteca de testes para Python.
  - SonarQube - Ferramenta de avaliação de código automática que detecta bugs, vulnerabilidades e 'code smells', utilizada para inspeção contínua.

- Conclusão

  - O projeto foi concluído com sucesso alinhado ao objetivo inicial que era desenvolver uma API que utilizasse Inteligência Artificial. Segundo uma pesquisa feita entre os membros da equipe, concluiu-se que seria interessante a utilização de filmes como objeto principal do trabalho. A base de dados da IMDB foi um fator determinante para essa escolha por ser uma biblioteca robusta, testada e consistente, o que nos ajudou muito nos passos iniciais de desenvolvimento.

### Projeto de inteligência artificial, para interação com a assistente virtual do primeiro semestre.

- [x] IA - lógica Fuzzy
- [x] Elaboração e distribuição da planilha para obtenção de dados - Dados para treinamento IA
- [x] Disponibilizar acesso da aplicação no Heroku
- [x] Rotas para acesso do assistente à aplicação
- [x] Banco e modelagem

### Quick Start

- Como fazer a instalação do projeto

  - Ter o Python instalado na sua máquina
  - Instalar um editor de texto da sua preferência (indicamos VSCode ou Pycharm)
  - Instalar o Docker desktop na sua máquina (há versões para Windows, Linux e Mac)
  - Fazer o clone do projeto em algum diretório da sua preferência
  - Entrar na pasta raiz do projeto através do comando "cd Topicos_Avancados"
  - Na pasta raiz executar o comando "docker-compose up"
  - Acessar a rota http://locahost:5001/getFilme/{algum número de 1 a 9}
  - Os números de 1 a 9 são os números de cada grupo que participa do Projeto Integrador
  
  - Adicionalmente foi incluído o SonarQube no projeto para análise de código, o container está preparado para iniciar em conjunto com o docker-compose e fica disponível em http://localhost:9000, os dados de acesso são login: admin e senha: admin (padrão do Sonar). Para ver a execução da análise é preciso seguir os passos do link https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/ e instalar o Sonar Scanner correspondente ao sistema operacional.
  Acessado o Sonar em localhost:9000 é preciso logar, criar um novo projeto com o nome r4u-app, gerar um token, escolher 'outra linguagem', o sistema operacional utilizado e rodar o comando gerado no diretório do projeto acessando via bash ou cmd.
  Os resultados da análise de código aparecem na aba Overview.

- Links úteis:
  - Python: https://www.python.org/
  - Docker: https://www.docker.com/
  - VSCode: https://code.visualstudio.com/
  - JetBrains: https://www.jetbrains.com/pt-br/pycharm/
  - Sonar Scanner: https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/

### Primeira entrega

- FlyWay como database automation;
- Deploy do código backend para a AWS;

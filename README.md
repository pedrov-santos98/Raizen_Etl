# Ecossistema para o Case da Raízen

### Ambiente para realizar o case prático da Raízen.
<br> Esse setup vai criar um sistema de containers contendo o airflow, postgrees, metabase além do airbyte para realizar o elt. Além disso é possível usar-lo de duas maneiras diferentes. Através de um script python que realiza todos os jobs pelo airflow ou usando o airbyte que será o responsável por inserir os dados no banco.
<br>  

Link da Documentação:  [Documentação](https://docs.google.com/document/d/1X4wLUmgpTCWniMyhzzsrDzr0UT9rlGfncI4Ss4JHcbo/edit?usp=sharing)

## Arquiteturas
![](https://i.postimg.cc/QdL8DDz0/arquitetura-sem-airbyte.jpg)
##
![](https://i.postimg.cc/bNSy4rmZ/arquitetura-com-airbyte.jpg)

## Dashboards
	  Vendas por Derivados de Petróleo 
![](https://uploaddeimagens.com.br/images/004/013/728/full/Dash_Vendas_Derivados.jpg?1662574847)

	  Vendas por Diesel

![enter image description here](https://uploaddeimagens.com.br/images/004/013/729/full/Dash_Vendas_Diesel.jpg?1662574951)
  

## OBJETIVO
O objetivo deste ambiente é realizar a extração de dados relacionados venda da petróleo e combustíveis do site do governo [ANP Dados Estatísticos](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos) processar e transformar o arquivo xls baixado e inserir os dados em um banco de dados Postgree para consumo do metabase e a geração de um relatório. Todo o script é controlado e executado em um ambiente airflow podendo ser configurado o processo do inicio ao fim pelo script Python ou o insert dos dados gerados pelo Airbyte (ELT) conforme as imagens acima.

## SETUP

#### Requisitos:
Primeiramente é necessário realizar a instalação do docker e do docker compose no ambiente.

 - Documentação para instalação:
	 - [Docker](https://docs.docker.com/engine/install/)
	 - [Docker Compose](https://docs.docker.com/compose/install/)

#### Em um terminal/DOS, dentro diretório docker, realizar o clone do projeto no github
          git clone -
          
## INICIANDO O AMBIENTE
   
### No terminal, no diretorio raizen_etl, executar os seguintes comandos
	sudo chmod +x start.sh
	sudo chmod +x stop.sh

### Depois execute
	./start.sh
#### Por padrão o script executa sem o ambiente do Airbyte. Caso queria usar o airbyte para realizar o elt edite o arquivo start.sh dentro da raiz do diretório e descomente as linhas comentadas.
	#!/bin/sh
	docker-compose build
	docker-compose up -d
	#cd ./airbyte -- Descomente
	#docker-compose up -d -- Descomente
	#sudo chown -R $USER /tmp/airbyte_local -- Descomente
#### Após descomentar salve o arquivo e execute o comando ./start.sh novamente

### Verificar os containers ativos
          docker container ls
### Possíveis problemas
	Um dos problemas mais comuns é relacionado ao docker-compose. 
	Caso verifique algum erro relacionado a versão do docker compose, faça a reinstalação do mesmo no seu ambiente.
	Outro problema pode ser algo relacionado ao "Docker Daemon" caso isso ocorra edite os script "start.sh" e "stop.sh" e adicione a palavra "sudo" na frente dos comandos do docker.
	       
## USANDO O AMBIENTE    
 ###   Abra o seu navegador e entre no airflow:
	 Digite na url -> localhost:8080
	 User: airflow
	 senha: airflow
 ###   Execute a dag "Raizen_etl" ou "Raizen_etl_airbyte" :
 ![enter image description here](https://uploaddeimagens.com.br/images/004/013/335/full/dags.jpg?1662511713)
 
 ### Para uso do Metabase e do Airbyte sugiro a leitura da documentação no link abaixo:
	Documentação

## Acesso WebUI dos Frameworks
 
* Airflow *http://localhost:8080*
* Metabase *http://localhost:3000*
* Airbyte *http://localhost:8000*

## Acesso JDBC

   ##### Postgre Acesso host
          jdbc:postgresql://localhost:5432/docker

   ##### Postgre Acesso via container interno
          jdbc:postgresql://172.17.0.1:5432/docker

## Usuários e senhas

   ##### Postgree
    Usuário: docker
    Senha: docker
    Db: docker

   ##### Metabase
    Usuário criado ao subir o docker-compose

   ##### Airflow
    Usuário: airflow
    Senha: airflow
   
   ##### Airbyte
    Usuário criado ao subir o docker-compose
 
## Documentação Oficial

* https://airflow.apache.org/
* https://www.metabase.com/docs/latest/
* https://docs.airbyte.com/
* https://airflow.apache.org/docs/

## Comandos Docker Importantes

### Parar um containers
         docker stop [nome do container]      

### Parar todos containers
         docker stop $(docker ps -a -q)
  
### Remover um container
         docker rm [nome do container]

### Remover todos containers
         docker rm $(docker ps -a -q)         

### Dados do containers
         docker container inspect [nome do container]

### Iniciar um container
         docker-compose up -d [nome do container]

### Iniciar todos os containers
         docker-compose up -d 

### Acessar log do container
         docker container logs [nome do container] 

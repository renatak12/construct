# Documento de Modelos


Neste documento temos o modelo de Dados (Entidade-Relacionamento). Temos também a descrição das entidades e o dicionário de dados.


## Modelo de Dados


Abaixo apresentamos o modelo dados (Entidade-Relacionamento) usando o **BrModelo**.


![Modelo Entidade-Relacionamento](images/modelo-conceitual-construct.png)


## Descrição das Entidades


A seguir temos uma breve descrição das entidades presentes no modelo e dos atributos que elas contém, assim como suas devidas finalidades.


### Entidade: Usuário


A entidade usuário armazena somente informações cruciais para a descrição do agente no sistema. Dentre as informações estão id do usuário. O username e senha para realizar o login no sistema. O cargo que especifica o tipo de usuário, como "administrador", "gerente", "vendedor". E o tipo de permissão de acesso do usuário no sistema, que determinam quais recursos e funcionalidades o usuário pode acessar.


### Entidade: Produto


Representa um produto disponível na loja. Cada produto tem um nome, uma descrição, um preço, um tipo, e uma quantidade em estoque.


### Entidade: Estoque


Essa entidade geralmente armazena informações sobre a quantidade disponível de produtos, a localização do estoque, as datas de chegada e saída dos produtos, entre outras informações importantes.


### Entidade: Cliente


Representa um cliente da loja. Cada cliente tem um nome, um telefone, um e-mail e um endereço. Um cliente pode ter várias vendas associadas a ele.


### Entidade: Venda


Representa uma venda realizada na loja. Cada venda tem uma data, um tipo, um preço, uma quantidade de produto escolhido, um valor total e um cliente associado. Uma venda pode ter vários itens de produtos associados a ela e gera um pagamento.


### Entidade: Pagamento


A entidade pagamento é geralmente usada para registrar as informações de pagamento feitas pelos clientes. Um pagamento pode ter id, data, valor total, tipo de pagamento, status de pagamento, etc. E está associada a um cliente e a uma venda.


### Entidade: Relatórios


Uma entidade relatório geralmente é usada para armazenar informações sobre relatórios que devem ser gerados pelo sistema. Um relatório tem um id, uma descrição e está associado a uma ou mais vendas.


## Dicionário de Dados


Dicionário de dados centraliza informações sobre o conjunto de dados (dataset) sob análise. Seu propósito é melhorar a comunicação entre todos os envolvidos no projeto, além de ser um repositório (documento) que descreve de forma estruturada, o significado, origem, relacionamento e uso dos dados.


## Tabela: Usuário


| Atributo  | Chave | Tipo de dado | Tamanho | Descrição                                     |
| --------- | :---: | :----------: | :-----: | --------------------------------------------- |
| id        |  PK   |   NUMERIC    |    4    | Identificador incremental de usuário.         |
| username      |  NN   | VARCHAR[100] |   256   | Email como username do usuário.                         |
| senha  |  NN   | VARCHAR[16]  |   16    | Senha para login do usuário.                |
| email     |  NN   | VARCHAR[256] |   256   | Email formato local-part@domain - - RFC 5322. |         |
| cargo  |  NN   | VARCHAR[16]  |   16    | Função do usuário.                |
| tipo_permissao     |  NN   | VARCHAR[256] |   16   |  Gerente ou vendedor.        |


## Tabela: Produto


| Atributo     | Chave | Tipo de dado | Tamanho | Descrição                                      |
| ------------ | :---: | :----------: | :-----: | ---------------------------------------------- |
| id           |  PK   |   NUMERIC    |    4    | Identificador incremental de produto.          |
| nome         |  NN   | VARCHAR[100] |   100   | Nome do produto.                               |
| descrição  |  NN   | VARCHAR[280] |   280   | Descrição do produto.                          |
| preço  |  NN   |     FLOAT     |    7    | Preço do produto.                     |
| tipo |  NN   |     VARCHAR[100]     |    100    | Tipo de produto                     |
| estoque  |  NN   |   NUMERIC   |    3    | Quantidade em estoque.            |                


## Tabela: Estoque


| Atributo     | Chave | Tipo de dado |  Tamanho  | Descrição                                                             |
| ------------ | :---: | :----------: | :-------: | --------------------------------------------------------------------- |
| id           |  PK   |   NUMERIC    |     4     | Identificador incremental de estoque.                                  |
| id_produto        |  FK   |   NUMERIC    |     4     | Chave para um produto.                                  |
| descricao         |  NN   |  VARCHAR[280]   | 280 | Descrição do produto.       |
| quantidade     |  NN   |   NUMERIC    |     4     | Quantidade em estoque.         |                    


## Tabela: Cliente


| Atributo    | Chave | Tipo de dado | Tamanho | Descrição                                                           |
| ----------- | :---: | :----------: | :-----: | ------------------------------------------------------------------- |
| id          |  PK   |   NUMERIC    |    6    | Identificador incremental de cliente.                              |
| nome    |  NN   |   VARCHAR[256]   |    256    | Nome do cliente. |
| telefone       |  NN   | VARCHAR[32]  |   32    | Telefone do cliente.                                                |
| endereço     |  NN   | VARCHAR[256] |   256   | Endereço do cliente.                                              |
| email |  NN   |   VARCHAR[256]    |    256    | Email do cliente. |


## Tabela: Venda


| Atributo     | Chave | Tipo de dado | Tamanho | Descrição                                      |
| ------------ | :---: | :----------: | :-----: | ---------------------------------------------- |
| id           |  PK   |   NUMERIC    |    4    | Identificador incremental de venda.          |
| datatime         |  NN   | DATATIME |   8   | Data e hora formato (YYYY-MM-DD HH:MM:SS.ffffff).                              |
| tipo_produto  |  NN   | VARCHAR[100] |   100   | Tipo de produto.                          |
| preço_produto  |  NN   |     FLOAT     |    7    | Preço do produto.                     |
| qntd_produto |  NN   |     VARCHAR[100]     |    100    | Quantidade de itens.                     |
| valor_total  |  NN   |   FLOAT   |    7    | Valor total da venda.    |
| cliente_id  |  FK   |   NUMERIC   |    6    | Chave para um cliente.  |


## Tabela: Pagamento


| Atributo     | Chave | Tipo de dado | Tamanho | Descrição                                      |
| ------------ | :---: | :----------: | :-----: | ---------------------------------------------- |
| id           |  PK   |   NUMERIC    |    4    | Identificador incremental de venda.          |
| datatime         |  NN   | DATATIME |   8   | Data e hora formato (YYYY-MM-DD HH:MM:SS.ffffff).                              |
| tipo_pagamento  |  NN   | VARCHAR[100] |   100   | Forma de pagamento.                          |
| status |  NN   |     VARCHAR[100]     |    100    | Aprovado, cancelado ou estornado.                 |
| valor_total  |  NN   |   FLOAT   |    7    | Valor total do pagamento.    |
| venda_id  |  FK   |   NUMERIC   |    4    | Chave para uma venda.  |
| cliente_id  |  FK   |   NUMERIC   |    6    | Chave para um cliente.  |


## Tabela: Relatório


| Atributo    | Chave | Tipo de dado | Tamanho | Descrição                                                           |
| ----------- | :---: | :----------: | :-----: | ------------------------------------------------------------------- |
| id          |  PK   |   NUMERIC    |    4    | Identificador incremental de venda.                              |
| descricao_relatorio   |  NN   |   VARCHAR[256]   |    256    | Descrição do relatório e seu propósito. |
| venda_id      |  FK   | NUMERIC  |   4   | Chave para uma venda.          |                                    


### Referências


[Exemplo de Dicionário - IBM](https://publib.boulder.ibm.com/tividd/td/ITMFTP/GC23-4803-00/pt_BR/HTML/TMTPmst80.htm)


[Dicionário de Dados](https://www.luis.blog.br/dicionario-de-dados.html)


[Dicionário de Dados Portal Dados Abertos](https://tce.pe.gov.br/internet/docs/dadosabertos/TomeConta2017DicionarioDados.pdf)


[Definição formal da estrutura de endereço de email](https://datatracker.ietf.org/doc/html/rfc5322)

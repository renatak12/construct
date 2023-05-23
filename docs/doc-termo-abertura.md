## TERMO DE ABERTURA DE PROJETO

## Histórico de revisões

| Data       | Versão |                           Descrição                            | Autor                          |
| :--------- | :----: | :------------------------------------------------------------: | :----------------------------- |
| 12/05/2023 | 1.0  |      Documento Inicial      | Annielly Ferreira de Souza       |

## 1. Equipe e Definição de Papéis

| Membro       | Papel                                      | E-mail                       | GitHub                                           |
| ------------ | ------------------------------------------ | ---------------------------- | ------------------------------------------------ |
| Annielly     | Gerente, Analista, Testador, Desenvolvedor | anniefs2021@gmail.com        |[Clique aqui](https://github.com/Anniellyfs)      |
| José Cláudio | Gerente, Analista, Testador, Desenvolvedor | zeclaudio_jr@yahoo.com.br    |[Clique aqui](https://github.com/ZeClaudio-Jr)    |
| Maicon       | Gerente, Analista, Testador, Desenvolvedor | marc.douglas630@gmail.com    |[Clique aqui](https://github.com/wanessabezerra)  |
| Raquel       | Gerente, Analista, Testador, Desenvolvedor | fernandeslimaraquel@gmail.com|[Clique aqui](https://github.com/fernandesraquel) |
| Renata       | Gerente, Analista, Testador, Desenvolvedor | renata.k.a@hotmail.co        |[Clique aqui](https://github.com/renatak12)       |

## 2.	Objetivos do projeto

O construct é um sistema de gestão para lojas de materiais de construção que visa o bom atendimento ao cliente, a gestão do estoque e o controle dos pedidos e finanças, além da emissão de relatórios.
O sistema permitirá o cadastro de informações da base de dados e das telas das funcionalidades para gerar relatórios.

## 3.	Justificativa do projeto

O Sistema construct facilita e agiliza as tarefas administrativas e operacionais de uma loja de materiais de construção, proporcionando uma visão abrangente das atividades e permitindo tomadas de decisão mais informadas. Com esse software, é possível reduzir erros, evitar perdas de estoque, melhorar a produtividade dos funcionários e, consequentemente, aumentar a satisfação dos clientes.

## 4.	Descrição dos produtos/entregáveis do projeto

| Documentos   
| Nome                                  | Link                                                 |
| ------------------------------------- | ---------------------------------------------------- |
| Plano de Iteração                     | [Clique aqui](docs/doc-plano-iteracao.md)            |
| Documento de Visão                    | [Clique aqui](docs/doc-visao.md)                     |
| Documento de Modelos                  | [Clique aqui](docs/doc-modelos.md)                   |
| Lista de User Stories                 | [Clique aqui](docs/doc-user-stories.md)              |
| Projeto Arquitetural do Software      | [Clique aqui](docs/doc-arquitetural.md)              |
| Análise de Pontos de Função - APF     | [Clique aqui](docs/doc-apf.md)                                                          |
| Termo de Abertura de Projeto          | [Clique aqui](docs/doc-termo-abertura.md)                                              |
| Relatório de Testes de Módulo/Sistema | [Clique aqui](docs/doc-us-tests.md)                                                     |

### Os módulos incluídos no sistema são:

1.	 Usuário: O usuário armazena somente informações cruciais para a descrição do agente no sistema. Dentre as informações estão id do usuário. O username e senha para realizar o login no sistema. O cargo que especifica o tipo de usuário, como "administrador", "gerente", "vendedor". E o tipo de permissão de acesso do usuário no sistema, que determinam quais recursos e funcionalidades o usuário pode acessar.

2.	Produto: Representa um produto disponível na loja. Cada produto tem um nome, uma descrição, um preço, um tipo, e uma quantidade em estoque.

3.	Estoque: Geralmente armazena informações sobre a quantidade disponível de produtos, a localização do estoque, as datas de chegada e saída dos produtos, entre outras informações importantes.

4.	Cliente: Representa um cliente da loja. Cada cliente tem um nome, um telefone, um e-mail e um endereço. Um cliente pode ter várias vendas associadas a ele.

5.	Venda: Representa uma venda realizada na loja. Cada venda tem uma data, um tipo, um preço, uma quantidade de produto escolhido, um valor total e um cliente associado. Uma venda pode ter vários itens de produtos associados a ela e gera um pagamento.

6.	Pagamento: É geralmente usada para registrar as informações de pagamento feitas pelos clientes. Um pagamento pode ter id, data, valor total, tipo de pagamento, status de pagamento, etc. E está associada a um cliente e a uma venda.

## 5.	Restrições para o projeto

- Acesso: App Mobile
- Acesso: Perfil social Autenticado (Ex.: Google, Facebook, Twitter, Discord)

## 6.	Cronograma de macros

### Plano de Iterações


| Iteração | Data início | Data Final | Apresentação | Gerente | Detalhes                                                                                                                                                                                                                               |
| -------- | ----------- | ---------- | ------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| It1      | 27/03/2023  | 13/04/2023 | 02/05/2023   | Renata | Criar Documento de Visão, Modelos e Plano de Iteração e Release, Detalhar User Story Base - US01, Estrutura do Projeto (código base)                 |
| It2      | 14/04/2023  | 04/05/2023 | 09/05/2023  | Raquel | Implementar US01, Testar US01, Detalhar US02 e US03, Criar Documento de Contagem por Pontos de Função, Criar documento Arquitetura Geral do Sistema e Termo de Abertura do Projeto                                                                                                                                                                           |
| It3      | 10/05/2023  | 25/05/2023 | 25/05/2023   | Annielly | Implementar US02, Testar US02, Implementar US03, Testar US03, Detalhar US04 e US05, Deploy do Release (Implantação), Atualizar documentos                                                                                                                           |
| It4      | 26/05/2023  | 22/06/2023 | 22/06/2023   | Maicon | Implementar US04, Testar US04, Implementar US05, Testar US05, Criar Relatório de Testes, Deploy do Release (Implantação), Atualizar documentos                                                                                                                                      |
| It5      | 23/06/2023  | 20/07/2023 | 20/07/2023   | José Cláudio | Atualizar Documento de Visão, Modelos, Plano de Iteração, Plano de Release, Documento de Contagem por Pontos de Função e Arquitetura Geral do Sistema, Implementar Testes |

### Plano de Release


| Release | Data início | Data Final | Gerente | Detalhes                                     |
| ------- | ----------- | ---------- | ------- | -------------------------------------------- |
| R01     | 27/03/2023  | 13/04/2023 | Renata | Lista de funcionalidades da Release 01 (It1) |
| R02     | 14/04/2023  | 04/05/2023 | Raquel | Lista de funcionalidades da Release 02 (It2) |
| R03     | 10/05/2023  | 25/05/2023 | Annielly | Lista de funcionalidades da Release 03 (It3) |
| R04     | 26/05/2023  | 22/06/2023 | Maicon  | Lista de funcionalidades da Release 04 (It4) |
| R05     | 23/06/2023  | 20/07/2023 | José Cláudio | Lista de funcionalidades da Release 05 (It5) |

## 7.	Partes interessadas

As partes interessadas do projeto são: os Gerente, Analista, Testador, Desenvolvedor, usuário e cliente.

## 8.	Riscos identificados

Tabela com o mapeamento dos riscos do projeto, consequência e providências a serem tomadas.

| Risco                                       | Consequências                                         |  Providência/Solução                  |
| ------------------------------------------- | ----------------------------------------------------- | ------------------------------------- | 
| Não aprendizado das ferramentas utilizadas  | Se os membros da equipe não aprenderem adequadamente as ferramentas necessárias para o projeto, eles podem enfrentar dificuldades na execução de suas tarefas. | Reforçar estudos sobre as ferramentas |
| Ausência por qualquer membro da equipe      | Quando um membro da equipe está ausente, seja por um curto período ou de forma permanente, pode haver lacunas na comunicação e colaboração. Isso pode resultar em informações perdidas, decisões tomadas sem a participação necessária e falta de alinhamento entre os membros da equipe. | Planejar o cronograma tendo em base a agenda dos membros. |
| Divisão de tarefas mal sucedida             | Se a divisão de tarefas não for feita de forma adequada, algumas áreas do projeto podem ser negligenciadas ou mal atendidas. Isso pode levar a erros, omissões e retrabalho, já que as responsabilidades não estão claramente definidas ou não são executadas corretamente. | Acompanhar de perto o desenvolvimento de cada membro da equipe. |

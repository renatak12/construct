# Documento Lista de User Stories

Documento construído a partido do **Modelo BSI - Doc 004 - Lista de User Stories** que pode ser encontrado no
link: <https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing>

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](doc-visao.md). Este documento também pode ser adaptado para descrever Casos de Uso. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão |                           Descrição                            | Autor                    |
| :--------- | :----: | :------------------------------------------------------------: | :----------------------- |
| 10/04/2023 | 1.0  |               Template e descrição do documento                | Renata Karla Araújo dos Santos |
| 02/05/2023 | 2.0  |                Detalhamento do User Story US01                 | Renata Karla Araújo dos Santos    |
| 11/05/2023 | 3.0  |                Detalhamento dos User Stories US02 e US03                 | Renata Karla Araújo dos Santos    |

### User Story US01 - Manter Usuário

|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | O sistema deve manter um cadastro de usuário que tem acesso ao sistema via login e senha. Um usuário tem os atributos name, id, email, username, data de nascimento, status, password. O email será o login e ele pode registrar-se diretamente no sistema. Além disso o usuário poderá alterar alguns dados, como o e-mail ou a senha. O usuário administrador do sistema pode realizar as operações de adicionar, alterar, remover e listar os usuários comuns do sistema. |

| **Requisitos envolvidos** |                                |
| ------------------------- | :----------------------------- |
| RF16                      | Cadastrar Usuário              |
| RF17                      | Alterar Usuário                |
| RF18                      | Consultar Usuário              |
| RF19                      | Vizualizar detalhes do Usuário |
| RF20                      | Excluir Usuário                |

|                         |           |
| ----------------------- | :-------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 8 h       |
| **Tempo Gasto (real):** |           |
| **Tamanho Funcional**   | 7 PF      |
| **Analista**   | Renata      |
| **Desenvolvedor**   | Renata      |
| **Revisor**   | Raquel      |
|**Testador**   | Annielly      |

### User Story US02 - Manter Produto

|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | O sistema deve manter um cadastro de produtos que serão gerenciados pelo sistema. Um produto tem os atributos id, nome, descrição, preço, tipo, e estoque. O usuário administrador do sistema pode realizar as operações de adicionar, alterar, remover e listar os produtos comuns do sistema. |

| **Requisitos envolvidos** |                                |
| ------------------------- | :----------------------------- |
| RF01                      | Cadastrar Produto              |
| RF02                      | Alterar Produto                |
| RF03                      | Consultar Produto              |
| RF04                      | Vizualizar detalhes do Produto |
| RF05                      | Excluir Produto                |

|                         |           |
| ----------------------- | :-------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 8 h       |
| **Tempo Gasto (real):** |           |
| **Tamanho Funcional**   | 7 PF      |
| **Analista**   | Renata      |
| **Desenvolvedor**   | Raquel      |
| **Revisor**   | Annielly      |
|**Testador**   | Maicon      |

### User Story US03 - Manter Estoque

|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | O sistema deve manter um estoque de produtos. Um estoque tem os atributos id, produto_id, descricao_produto, quantidade. O estoque deverá atualizar de acordo com as entradas e saídas de produtos. O usuário administrador do sistema pode realizar as operações de adicionar, alterar, remover e listar os produtos em estoque do sistema. |

| **Requisitos envolvidos** |                                |
| ------------------------- | :----------------------------- |
| RF21                      | Cadastrar Estoque              |
| RF22                      | Alterar Estoque                |
| RF23                      | Consultar Estoque              |
| RF24                      | Vizualizar detalhes do Estoque |
| RF25                      | Excluir Estoque                |

|                         |           |
| ----------------------- | :-------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 8 h       |
| **Tempo Gasto (real):** |           |
| **Tamanho Funcional**   | 7 PF      |
| **Analista**   | Renata      |
| **Desenvolvedor**   | Raquel      |
| **Revisor**   | Maicon      |
|**Testador**   | José Claudio      |



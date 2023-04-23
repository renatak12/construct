# Documento Lista de User Stories

Documento construído a partido do **Modelo BSI - Doc 004 - Lista de User Stories** que pode ser encontrado no
link: <https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing>

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](doc-visao.md). Este documento também pode ser adaptado para descrever Casos de Uso. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão |                           Descrição                            | Autor                    |
| :--------- | :----: | :------------------------------------------------------------: | :----------------------- |
| 10/03/2023 | 0.0.1  |               Template e descrição do documento                | Renata Karla Araújo dos Santos |
| 11/03/2023 | 0.0.2  |                Detalhamento do User Story US01                 | Renata Karla Araújo dos Santos    |
| 23/04/2023 | 0.0.3  |                Testes do User Story US01                 | Renata Karla Araújo dos Santos    |

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

| Testes de Aceitação (TA) |                                                                                                                                                                                                                                                                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Código**               | **Descrição**                                                                                                                                                                                                                                                                                                                                |
| **TA01.01**              | O usuário é redirecionado para a página de login social e tudo ocorre corretamente. Ele é redirecionado para a tela de boas-vindas da plataforma.                                                                                                                                                                                            |
| **TA01.02**              | O usuário é redirecionado para a página de login social e autenticação social falha. É exibida a mensagem: "Não foi possível realizar o login, Tente novamente". O usuário é redirecionado para a tela de login.                                                                                                                             |
| **TA01.03**              | O usuário solicita a exclusão de seu perfil na página de visualização de detalhes, uma notificação de confirmação é exibida em modal ou toast, a exclusão é realizada e a mensagem "Perfil excluído com sucesso" é exibida. O usuário é redirecionado para a tela principal.                                                                 |
| **TA01.04**              | O usuário solicita a exclusão de seu perfil na página de visualização de detalhes, a exclusão não ocorre e a mensagem "Tente novamente" é exibida. O usuário é redirecionado para a página de visualização de detalhes de usuário.                                                                                                           |
| **TA01.05**              | O usuário, na tela de detalhes, realiza alterações nas informações e seleciona para salvar,tudo ocorre corretamente e a mensagem "Tudo Certo!" é exibida. O usuário é redirecionado para a tela de detalhes com as novas informações.                                                                                                         |
| **TA01.06**              | O usuário, na tela de detalhes, realiza alterações nas informações e seleciona para salvar,ocorre uma falha na atualização e a mensagem "Problemas técnicos, Tente novamente..." é exbida. O usuário continua na mesma tela até solicitar para salvar novamente ou cancelar as alterações.                                                   |
| **TA01.07**              | O usuário, na tela de detalhes, realiza alterações nas informações e seleciona para salvar, o usuário preenche incorretamente alguma informação e a mensagem "Ops! Tem alguma coisa errada, verifique os dados e tente novamente". O usuário continua na mesma tela até alterar e solicitar para salvar novamente ou cancelar as alterações. |

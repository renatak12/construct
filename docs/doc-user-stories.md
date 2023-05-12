# Documento Lista de User Stories

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](doc-visao.md). Este documento também pode ser adaptado para descrever Casos de Uso. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão |                           Descrição                            | Autor                          |
| :--------- | :----: | :------------------------------------------------------------: | :----------------------------- |
| 10/04/2023 | 1.0.0  |               Template e descrição do documento                | Renata Karla Araújo dos Santos |
| 02/05/2023 | 2.0.0  |                Detalhamento do User Story US01                 | Renata Karla Araújo dos Santos |
| 08/05/2023 | 3.0.0  |                Detalhamento do User Story US02                 | Raquel Lima Fernandes          |
| 10/05/2023 | 4.0.0  |               Inserção dos testes de aceitação                 | Raquel Lima Fernandes          |
| 11/05/2023 | 5.0.0  |                Detalhamento do User Story US03                 | Renata Karla Araújo dos Santos |

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

| Testes de Aceitação (TA) |                                                                                                                                                                                                                                                                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Código**               | **Descrição**                                                                                                                                                                                                                                                                                                                                |
| **TA01.01**              | O usuário é redirecionado para a página de login social e tudo ocorreu corretamente. Ele é redirecionado para a tela de boas-vindas da plataforma.                                                                                                                                                                                            |
| **TA01.02**              | O usuário é redirecionado para a página de login social e autenticação social falha. É exibida a mensagem: "Não foi possível realizar o login, Tente novamente". O usuário é redirecionado para a tela de login.                                                                                                                             |
| **TA01.03**              | O usuário solicita a exclusão de seu perfil na página de visualização de detalhes, uma notificação de confirmação é exibida, a exclusão é realizada e a mensagem "Perfil excluído com sucesso" é exibida.                                                                |                                                                                                                                                                                                                 
| **TA01.04**              | O usuário, na tela de detalhes, realiza alterações nas informações e seleciona para salvar, o usuário preenche incorretamente alguma informação e a mensagem "Ops! Tem alguma coisa errada, verifique os dados e tente novamente". O usuário continua na mesma tela até alterar e solicitar para salvar novamente ou cancelar as alterações. |





<table>
  <thead>
    <tr>
      <th colspan="4" scope="row">User Story US02 - Manter Produto</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row"><b>Descrição</b></td>
      <td colspan="3">Como gerente de uma loja de materiais de construção,
        quero ser capaz de manter uma lista atualizada de produtos,
        para que eu possa gerenciar meu estoque de maneira eficiente e atender às necessidades dos clientes.
</td>
    </tr>
    <tr>
      <td scope="row"><b>Requisistos Envolvidos<b/></td>
      <td colspan="3">RF001, RF002, RF003, RF004, RF005 e RF006</td>
    </tr>
    <tr>
      <td scope="row"><b>Prioridade</b></td>
      <td colspan="3">Essencial</td>
    </tr>
    <tr>
      <td scope="row"><b>Estimativa<b/></td>
      <td>5h</td>
      <td><b>Tempo Gasto (real):<b/></td>
      <td>5h</td>
    </tr>
    <tr>
      <td scope="row"><b>Analista<b/></td>
      <td colspan="3">Raquel (responsável por especificar/detalhar o US).</td>
    </tr>
    <tr>
      <td scope="row"><b>Desenvolvedor<b/></td>
      <td colspan="3">Annielly (responsável por implementar e realizar testes de unidade e testes de integração).</td>
    </tr>
    <tr>
      <td scope="row"><b>Revisor<b/></td>
      <td colspan="3">José Cláudio (responsável por avaliar a implementação e executar os testes de unidade e testes de integração).</td>
    </tr>
    <tr>
      <td scope="row"><b>Testador<b/></td>
      <td colspan="3">Renata (responsável por executar os Testes de Aceitação e fazer o relatório de testes).</td>
    </tr>
    <tr>
      <th colspan="4" scope="row">Testes de Aceitação (TA)</th>
    </tr>
    <tr>
      <td scope="row"><b>Código</b></td>
      <th colspan="3">Descrição</th>
    </tr>
    <tr>
      <td scope="row"><b>TA01.01<b/></td>
      <td colspan="3">Como gerente da loja, quando eu acessar a página para adicionar um novo produto, devo ser capaz de preencher todos os campos obrigatórios, incluindo nome, descrição, categoria, preço, estoque, imagem e outras informações relevantes. Ao clicar em "Salvar", devo ser notificado com uma mensagem de sucesso: <em>"Produto adicionado com sucesso"</em>. O produto deve ser exibido na lista de produtos disponíveis na loja.</td>
    </tr>
    <tr>
      <td scope="row"><b>TA01.02</b></td>
      <td colspan="3">Como gerente da loja, ao acessar a página para editar as informações de um produto, devo ser capaz de editar todos os campos do produto, incluindo nome, descrição, categoria, preço, estoque, imagem e outras informações relevantes. Ao clicar em "Salvar", as alterações devem ser salvas com sucesso e as informações do produto devem ser atualizadas na lista de produtos disponíveis na loja.</td>
    </tr>
    <tr>
      <td scope="row"><b>TA01.03</b></td>
      <td colspan="3">Como gerente da loja, quando eu acessar a página de listagem de produtos, devo ser capaz de selecionar um produto para exclusão. Quando eu clicar em "Excluir", o produto deve ser excluído com sucesso e uma mensagem: <em>"Produto excluído com sucesso"</em> deve ser exibida na tela. Após a exclusão, o produto não deve mais ser exibido na lista de produtos disponíveis na loja.</td>
    </tr>
    <tr>
      <td scope="row"><b>TA01.04</b></td>
      <td colspan="3">Como gerente da loja, quando eu acessar a página de listagem de produtos, devo ser capaz de visualizar todos os produtos existentes na loja. Ao clicar em um produto, devo ser direcionado para a página de detalhes do produto, e as informações do produto devem ser exibidas corretamente, incluindo nome, descrição, categoria, preço, estoque, imagem e outras informações relevantes.</td>
    </tr>
    <tr>
      <td scope="row"><b>TA01.05</b></td>
      <td colspan="3">Como gerente da loja, quando tento adicionar ou editar informações de um produto, todos os campos obrigatórios devem ser validados. Se inserir dados inválidos em algum campo, exibirá uma mensagem de erro: <em>"Campos incorretos"</em> e o produto não será adicionado ou editado até que todos os campos sejam preenchidos corretamente. Se o estoque de um produto for menor que zero, exibirá uma mensagem de erro informando que o produto está fora de estoque: <em>"Produto fora de estoque"</em>.
      </td>
    </tr>
  </tbody>
</table>

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

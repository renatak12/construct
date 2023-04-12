# Documento de Visão

## Histórico de Revisões 

| Data       | Versão | Descrição                                   | Autor(es)                |
| ---------- | ------ | ------------------------------------------- | ------------------------ |
| 08/04/2021 | 1.0    | Documento Inicial                           | Raquel Lima Fernandes    |

## Equipe e Definição de Papéis

| Membro       | Papel                                      | E-mail                       | GitHub                                           |
| ------------ | ------------------------------------------ | ---------------------------- | ------------------------------------------------ |
| Annielly     | Gerente, Analista, Testador, Desenvolvedor | anniefs2021@gmail.com        |[Clique aqui](https://github.com/Anniellyfs)      |
| José Cláudio | Gerente, Analista, Testador, Desenvolvedor | zeclaudio_jr@yahoo.com.br    |[Clique aqui](https://github.com/ZeClaudio-Jr)    |
| Maicon       | Gerente, Analista, Testador, Desenvolvedor | marc.douglas630@gmail.com    |[Clique aqui](https://github.com/wanessabezerra)  |
| Raquel       | Gerente, Analista, Testador, Desenvolvedor | fernandeslimaraquel@gmail.com|[Clique aqui](https://github.com/fernandesraquel) |
| Renata       | Gerente, Analista, Testador, Desenvolvedor | renata.k.a@hotmail.co        |[Clique aqui](https://github.com/renatak12)       |

## Matriz de Competências

| Membro       | Competências                                                                                                      |
| ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Annielly     | Software Tester Desenvolvedora JavaScript, Python                                                                 |
| José Cláudio | Desenvolvedor Javascript, Python                                                                                  |
| Maicon       | Desenvolvedor Python, Django, JavaScript                                                                          |
| Raquel       | Gerente e Desenvolvedora Javascript, React, Nexjtjs, Python, C, PostgreSQL                                        |  
| Renata       | Desenvolvedora Javascript, Python, Django                                                                         |

## Perfis dos Usuários

O sistema poderá ser utilizado por usuários. Temos os seguintes perfis/atores:

| Perfil        | Descrição                                                                                                                                                      |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gerente       | Este usuário utiliza as funções de cadastro, edição, alteração e exclusão de produtos, assim como emiti relatórios.                                            |
| Vendedor      | Este usuário utiliza as funções de cadastro, edição, alteração e exclusão de clientes, assim como realiza vendas e realiza orçamentos.                         |
| Caixa         | Este usuário utiliza as funções de abrir e fechar caixa, assim como finalizar uma compra.                                                                      |

## Lista de Requisitos Funcionais

| Requisito                                         | Descrição                                                                   | Ator     |
| ------------------------------------------------- | --------------------------------------------------------------------------- | -------- |
| RF01 - Incluir Produto                            | Um produto tem os atributos nome, quant_estoque, marca, preco               | Gerente  |
| RF02 - Alterar Produto                            | A alteração permite a mudança de todos os atributos de um produto           | Gerente  |
| RF03 - Listar Produto                             | Lista todos os produtos cadastrados                                         | Gerente  | 
| RF04 - Visualizar Produto                         | Visualiza todas as informações sobre um produto específico                  | Gerente  |
| RF05 - Excluir Produto                            | Remove produtos                                                             | Gerente  |
| RF06 - Emitir Relatório                           | Emiti relatórios semanais, mensais e anuais                                 | Gerente  | 
| RF07 - Incluir Cliente                            | Um cliente tem os atributos nome, cpf, endereço, telefone                   | Vendedor |
| RF08 - Alterar Cliente                            | A alteração permite a mudança de todos os atributos de um cliente           | Vendedor |
| RF09 - Listar Cliente                             | Lista todos os clientes cadastrados                                         | Vendedor |
| RF10 - Visualizar Cliente                         | Visualiza as informações de um cliente específico                           | Vendedor |
| RF11 - Excluir Cliente                            | Remove um cliente                                                           | Vendedor |
| RF11 - Realizar Venda                             | Realiza uma venda                                                           | Vendedor |
| RF12 - Realizar Orçamento                         | Realiza orçamentos para uma venda                                           | Vendedor |
| RF13 - Abir caixa                                 | Abre  o caixa                                                               | Caixa    |
| RF14 - Fechar caixa                               | Fecha o caixa                                                               | Caixa    |
| RF15 - Finalizar compra                           | Finaliza uma compra                                                         | Caixa    |
| RF16 - Incluir Usuário                            | Um usuário contém nome, email, username e data de nascimento               | Gerente  |
| RF17 - Alterar Usuário                            | Altera dados cadastrais do usuário          | Gerente  |
| RF18 - Listar Usuário                            | Exibe as informações básicas do usuário cosultado                                         | Gerente  | 
| RF19 - Visualizar Usuário                        | Exibe as informações detalhadas do usuário                 | Gerente  |
| RF20 - Excluir Usuário                            | Remove a conta do usuário do sistema                                        | Gerente  |

## Lista de Requisitos Não-Funcionais

| Requisito                                    | Descrição                                                                                    |
| -------------------------------------------- | -------------------------------------------------------------------------------------------- |
| RNF001 - Consultas deve ser eficiente        | O sistema deve executar as consultas em milessegundos.                                       |
| RNF002 - Log de acesso                       | Deve manter um log de todos os acessos.                                                      |

## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

| Data       | Risco                                                                  | Prioridade | Responsável | Status  | Providência/Solução                                            |
| ---------- | ---------------------------------------------------------------------- | ---------- | ----------- | ------- | -------------------------------------------------------------- |
| 08/04/2023 | Não aprendizado das ferramentas utilizadas pelos componentes da equipe | Alta       | Gerente     | Vigente | Reforçar estudos sobre as ferramentas.                         |
| 08/04/2023 | Ausência por qualquer membro da equipe                                 | Média      | Gerente     | Vigente | Planejar o cronograma tendo em base a agenda dos membros.      |
| 08/04/2023 | Divisão de tarefas mal sucedida                                        | Baixa      | Gerente     | Vigente | Acompanhar de perto o desenvolvimento de cada membro da equipe |


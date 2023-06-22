<h1>Documento de Visão</h1>

<h2>Sumário</h2>

- [1. Introcução](#1-introdução)
  - [1.1. Histórico de revisões](#11-histórico-de-revisões)
- [2. Descrição do Sistema](#2-descrição-do-sistema)
- [3. Matriz de Competências](#3-matriz-de-competências)
- [4. Perfis dos Usuários](#4-perfis-dos-usuários)
- [5. Lista de Requisitos Funcionais](#5lista-de-requisitos-funcionais)
- [6. Lista de Requisitos Não-Funcionais](#6-lista-de-requisitos-não-funcionais)
- [7. Restrições e Limitações](#7-restrições-e-limitações)
- [8. Gestão de Riscos](#8-gestão-de-riscos)
- [9. Considerações Finais](#9-considerações-finais)


## 1. Introdução

O objetivo deste projeto é desenvolver um sistema de gestão para lojas de materiais de construção, denominado **CONSTRUCT**, utilizando o framework Django e a linguagem Python. O sistema fornecerá recursos de cadastro, listagem, busca, exclusão, edição, controle de estoque, vendas, relatórios e emissão de nota fiscal. Este documento descreve a visão geral do projeto, incluindo a descrição do sistema, matriz de competências, perfis dos usuários, lista de requisitos funcionais, lista de requisitos não-funcionais, restrições e limitações, gestão de riscos, modelo conceitual e considerações finais.

## 1.1. Histórico de Revisões

|Data|	Versão|	Descrição|	Autor(es)|
|---|---|---|---|
|08/04/2023|	1.0.0|	Documento Inicial|	Raquel Lima Fernandes|
|09/05/2023|	2.0.0|	Mudança nos RF e RNF|	Raquel Lima Fernandes|
|15/05/2023|	3.0.0|	Acrescentando DER|	Raquel Lima Fernandes|
|23/05/2023|	4.0.0|	Atualizando Documento|	Renata Karla Araújo dos Santos|
|20/06/2023|	5.0.0|	Documento Final Atualizado|	Raquel Lima Fernandes|

## 2. Descrição do Sistema

O sistema **CONSTRUCT** será uma aplicação web que permitirá o gerenciamento eficiente das atividades relacionadas à loja de materiais de construção. Os principais módulos incluem o cadastro, listagem, busca e exclusão de gerente, vendedores, fornecedores e clientes, controle de estoque, registro de vendas, emissão de nota fiscal e geração de relatórios. O sistema será desenvolvido com o framework Django, proporcionando uma arquitetura robusta e escalável.

## 3. Matriz de Competências

O desenvolvimento deste sistema requer as seguintes competências técnicas:
|Competência| 	Descrição|
|---|---|
|Conhecimento em programação Python|	Os desenvolvedores devem possuir habilidades sólidas em programação Python, incluindo conhecimento de sintaxe, estruturas de dados, funções e módulos.|
|Experiência com o framework Django|	O desenvolvimento do sistema será baseado no framework Django, portanto, é necessário que a equipe possua experiência em sua utilização, isso inclui familiaridade com conceitos como models, views, templates, rotas, autenticação, entre outros recursos fornecidos pelo Django.|
|Familiaridade com bancos de dados relacionais|	O sistema de gestão para lojas de materiais de construção exigirá o uso de um banco de dados relacional para armazenar informações, como cadastro de funcionarios, produtos, vendas e clientes. A equipe de desenvolvimento deve ter conhecimentos sólidos em bancos de dados relacionais, como modelagem de dados, SQL e gerenciamento de conexões.|
|Habilidades em design de banco de dados|	É fundamental ter habilidades em design de banco de dados para criar uma estrutura adequada que atenda aos requisitos do sistema. Isso inclui a definição de tabelas, relacionamentos entre entidades, normalização e otimização de consultas.|
|Conhecimentos em web development|	O sistema será uma aplicação web, portanto, conhecimentos em tecnologias web, como HTML, CSS e JavaScript, serão úteis para o desenvolvimento da interface do usuário e aprimoramento da experiência do cliente.|
|Conhecimento em segurança da informação|	Dada a sensibilidade dos dados do cliente e a necessidade de proteger o sistema contra ameaças, é importante ter conhecimentos em segurança da informação. Isso inclui a implementação de práticas adequadas de autenticação, autorização, criptografia e prevenção de ataques.|

## 4. Perfis dos Usuários

|Perfil|	Descrição|
|---|---|
|Gerente|	Responsável por administrar o sistema e ter acesso completo a todas as funcionalidades. Poderá cadastrar vendedores, fornecedores, clientes, produtos, etc.|
|Vendedor|	Poderá registrar vendas, consultar estoque, visualizar informações de clientes e emitir notas fiscais. Terá permissões limitadas para as atividades relacionadas à gestão do sistema.|
|Fornecedor|	Não utilizará as funcionalidades do sistema, mas poderá ter seus dados cadastrados e gerenciados pelo gerente.|
|Cliente|	Não utilizará as funcionalidades do sistema, mas poderá ter seus dados cadastrados e gerenciados pelo gerente e/ou vendedor.|

## 5.Lista de Requisitos Funcionais

|Requisito| 	Descrição|	Ator|
|---|---|---|
|RF001 - Cadastro de Gerente|	O sistema permitirá o cadastro do gerente, fornecendo informações pessoais e credenciais de acesso.|	TI|
|RF002 - Cadastro de Vendedores|	O sistema permitirá o cadastro de vendedores, fornecendo informações pessoais e atribuindo permissões de acesso.|	Gerente|
|RF003 - Cadastro de Fornecedores|	O sistema permitirá o cadastro de fornecedores, fornecendo informações como nome, endereço e dados de contato.|	Gerente|
|RF004 - Cadastro de Clientes|	O sistema permitirá o cadastro de clientes, registrando suas informações pessoais, endereço e histórico de compras.|	Gerente e Vendedor|
|RF005 - Cadastro de Produtos|	O sistema permitirá o cadastro de produtos, incluindo informações como nome, descrição, código, preço e quantidade em estoque.|	Gerente|
|RF006 - Controle de Estoque|	O sistema registrará as entradas e saídas de produtos, atualizando automaticamente as quantidades disponíveis.|	Gerente e Vendedor|
|RF007 - Registro de Vendas|	O sistema registrará as vendas realizadas, associando os produtos vendidos aos respectivos clientes registrando o valor total da venda.|	Gerente e Vendedor|
|RF008 - Geração de Relatórios|	O sistema deve ser capaz de gerar  relatórios de vendas diárias, vendas por período, desempenho dos vendedores e estoque atual.|	Gerente e Vendedor|
|RF09 - Busca de Informações|	O sistema deve permitir a busca de informações sobre vendedores, fornecedores, clientes, produtos e estoque com base em critérios específicos, como nome, código, ou outras informações relevantes.|	Gerente e Vendedor|
|RF010 - Exclusão de Registros|	O sistema deve permitir a exclusão de registros de vendedores, fornecedores, clientes e produtos caso necessário.|	Gerente |
|RF011 - Edição de Registros|	O sistema deve permitir a edição dos dados de vendedores, fornecedores, clientes, produtos e estoque, sempre que necessário.|	Gerente e Vendedor|

## 6. Lista de Requisitos Não-Funcionais

|Requisito|	Descrição|
|---|---|
|RNF01 - Usabilidade|	O sistema deve possuir uma interface intuitiva e de fácil utilização, garantindo que os usuários possam navegar e executar tarefas de forma eficiente.|
|RNF02 - Desempenho|	O sistema deve ser capaz de lidar com um grande volume de dados, garantindo resposta rápida em todas as funcionalidades.|
|RNF03 - Segurança|	O sistema deve garantir a segurança dos dados armazenados, implementando mecanismos de autenticação e autorização para controlar o acesso às informações.|
|RNF04 - Confiabilidade|	O sistema deve ser confiável e estar disponível para uso durante a maior parte do tempo, minimizando as chances de interrupções ou falhas.|
|RNF05 - Escalabilidade|	O sistema deve ser projetado para permitir o crescimento e a adição de novos recursos no futuro, conforme necessário.|

## 7. Restrições e Limitações

O projeto possui as seguintes restrições e limitações:

1. Tecnologia: O sistema será desenvolvido utilizando o framework Django e a linguagem de programação Python.
2. Ambiente de Implantação: O sistema será implantado em um servidor web com suporte a Django e Python.
3. Escopo: O sistema será focado nas funcionalidades relacionadas à gestão de lojas de materiais de construção.

## 8. Gestão de Riscos 

|Data|	Risco	Prioridade|	Responsável|	Status|	Solução|
|---|---|---|---|---|
|01/05/23|	Atraso na entrega dos equipamentos de hardware|	Alta|	Gerente|	Aberto|	Entrar em contato com o fornecedor para obter um posicionamento e considerar alternativas de fornecimento ou ajuste de prazos.|
|10/05/23|	Falta de recursos técnicos qualificados|	Média|	Gerente|	Em andamento|	Iniciar processo de contratação ou treinamento da equipe para preencher a lacuna de habilidades necessárias.|
|20/05/23|	Vulnerabilidade de segurança identificada|	Alta|	TI|	Resolvido|	Aplicar patches e atualizações de segurança para corrigir a vulnerabilidade identificada e monitorar regularmente a segurança do sistema.|
|30/05/23|	Mudança nos requisitos do cliente|	Alta|	Gerente|	Aberto|	Realizar reunião com o cliente para entender as mudanças necessárias e avaliar o impacto nos prazos e custos do projeto.|
|05/06/23|	Interrupção no fornecimento de energia elétrica|	Média|	Gerente|	Aberto|	Estabelecer um plano de contingência com um gerador de energia ou fonte alternativa para minimizar o impacto de possíveis interrupções.|
|10/06/23|	Instabilidade no provedor de hospedagem|	Alta|	TI|	Aberto|	Avaliar alternativas de provedores de hospedagem, realizar testes de desempenho e confiabilidade e implementar medidas de backup para evitar perda de dados.|
|20/06/23|	Falha no processo de backup dos dados|	Alta|	TI|	Em andamento|	Revisar e aprimorar o processo de backup, realizar testes regulares de restauração e implementar mecanismos de monitoramento para garantir a eficácia do backup.|
|30/06/23|	Conflitos de agenda entre os membros da equipe|	Baixa|	Gerente|	Resolvido|	Implementar um sistema de gerenciamento de calendário compartilhado e estabelecer políticas de comunicação e coordenação entre a equipe.|

## 9. Considerações Finais

O sistema **CONSTRUCT** visa proporcionar uma solução eficiente e abrangente para a administração de lojas do setor de materiais de construção. Ao permitir o cadastro de produtos, controlar o estoque, registrar vendas, gerar relatórios e emitir notas fiscais, o sistema oferecerá suporte às operações diárias das lojas. Utilizando o framework Django e Python, espera-se alcançar uma implementação robusta e escalável. A gestão de riscos é um fator essencial para garantir a segurança e o desempenho do sistema, e a integração com outros sistemas existentes deve ser considerada durante o desenvolvimento. Com essas diretrizes em mente, o sistema de gestão ajudará as lojas de materiais de construção a otimizar suas operações e aprimorar a experiência do cliente.

# **Análise de Pontos de Função para o Sistema Construct**  


A Análise de Pontos de Função (APF) é uma técnica de estimativa de tamanho de software baseada em suas funcionalidades. Ela é utilizada para medir o tamanho funcional de um software e pode ser aplicada a sistemas novos ou já existentes. Também posicionamos a APF em relação à norma ISO 14143. Isso é importante, porque padroniza os requisitos para um método de medição do tamanho funcional e permite a você entender melhor o impacto ao interpretar dados expressos em pontos de função. Para realizar uma APF, é necessário seguir os seguintes passos:

1. Identificar as funções do sistema: as funções são as operações que o software deve realizar. Elas podem ser divididas em três tipos: funções de dados, funções de transação e funções de referência. É importante listar todas as funções do sistema para garantir que nada seja esquecido.

2. Avaliar a complexidade das funções: cada função deve ser avaliada em termos de sua complexidade. Para isso, são considerados os seguintes fatores: número de inputs, número de outputs, número de arquivos lógicos referenciados, número de consultas e complexidade da lógica interna.

3. Atribuir pontos às funções: cada tipo de função tem um peso diferente em relação aos fatores de complexidade. Por exemplo, uma função de transação com muitos inputs e outputs terá mais pontos do que uma função de dados com poucos inputs e outputs. Os pontos são calculados de acordo com uma tabela de pesos, que é geralmente fornecida pela organização que desenvolveu a técnica.

4. Calcular o total de pontos de função: somam-se os pontos de todas as funções para obter o total de pontos de função do sistema.

5. Converter pontos de função em tamanho em linhas de código: os pontos de função são convertidos em tamanho em linhas de código usando um fator de conversão. Esse fator varia de acordo com a linguagem de programação e a tecnologia utilizada no desenvolvimento do software.

A APF é uma técnica bastante útil para estimar o tamanho de um software de forma objetiva e independente da tecnologia utilizada. No entanto, é importante lembrar que ela não leva em conta outros fatores importantes para o sucesso de um projeto de software, como a qualidade do código, a experiência da equipe de desenvolvimento e a complexidade do ambiente em que o software será utilizado. Por isso, é importante usar a APF como uma ferramenta complementar a outras técnicas de gestão de projetos de software.



## **Descrição do Projeto**  

O construct é um sistema de gestão para lojas de materiais de construção que visa o bom atendimento ao cliente, a gestão do estoque e o controle dos pedidos e finanças, além da emissão de relatórios.    
	 O sistema permitirá o cadastro de informações da base de dados e das telas das funcionalidades para gerar relatórios.  

## **Siglas**  
    PF - Pontos de Função  
    APF - Análise de Pontos de Função  
    ALI - Arquivos Lógicos Internos
    AIE - Arquivos de Interface Externa
    RF - Requisito Funcional


## **Lista de User Stores (US)**  
Lista de User Stores e requisitos a ela associados.  

US01 - Manter Usuário  
* RF0016 - Cadastrar Usuário
* RF0017 - Alterar Usuário
* RF0018 - Consultar Usuários
* RF0019 - Vizualizar detalhes do Usuário
* RF0020 - Excluir Usuário  

US02 - Manter Produto  
* RF0001 - Incluir Produto
* RF0002 - Alterar Produto
* RF0003 - Listar Produtos
* RF0004 - Vizualizar detalhes do Produto
* RF0005 - Excluir Produto
* RF0006 - Emitir Relatórios  

US03 - Manter Estoque  
* RF0021 - Cadastrar Estoque
* RF0022 - Alterar Estoque
* RF0023 - Consultar Estoques
* RF0024 - Vizualizar detalhes do Estoque
* RF0025 - Excluir Estoque  

US04 - Manter Cliente  
* RF0007 - Incluir Cliente
* RF0008 - Alterar Cliente
* RF0009 - Listar Clientes
* RF0010 - Vizualizar detalhes do Cliente
* RF0011 - Excluir Cliente  

US05 - Manter Venda  
* RF0026 - Incluir Venda
* RF0027 - Alterar Venda
* RF0028 - Listar Vendas
* RF0029 - Vizualizar detalhes do Venda
* RF0030 - Excluir Venda


## **Tipos de contagem**  
### Contagem Indicativa (Ci) - (Tipo de Contagem Escolhida)  
Em Administração de Projetos de Software, "Contagem Indicativa" (CI) é uma técnica utilizada na Análise de Pontos de Função (APF) para obter uma estimativa aproximada do tamanho e complexidade do software a ser desenvolvido.  

A Contagem Indicativa é feita com base em informações de alto nível sobre o projeto, como descrições de requisitos, casos de uso ou protótipos. Com base nessas informações, o analista de pontos de função faz uma avaliação rápida e aproximada do número de funcionalidades do sistema e de sua complexidade, para obter uma estimativa preliminar da quantidade de pontos de função que serão contados.

Essa estimativa preliminar pode ser usada para avaliar a viabilidade do projeto, estimar o custo e o prazo de desenvolvimento e ajudar na definição do escopo do projeto. No entanto, é importante ressaltar que a Contagem Indicativa não substitui a Contagem Detalhada de Pontos de Função, que é realizada posteriormente, com base em informações mais precisas e detalhadas sobre o software a ser desenvolvido. 

Na contagem indicativa (Ci) só é necessário conhecer e analisar as Funções de Dados. Desta forma, os ALIs (Arquivos Lógicos Internos) com o valor de 35 PF cada e os AIEs (Arquivos de Interface Externa) com o valor de 15 PF cada.

### Contagem Estimativa (Ce)  
"Contagem Estimativa" (CE) é outra técnica utilizada na Análise de Pontos de Função (APF) para obter uma estimativa aproximada do tamanho e complexidade do software a ser desenvolvido.

A Contagem Estimativa é realizada quando não há informações suficientes para uma contagem precisa de pontos de função, como na fase inicial de um projeto, ou quando há incertezas significativas sobre os requisitos e funcionalidades do software.

Nessa técnica, o analista de pontos de função utiliza sua experiência e conhecimento prévio para estimar a quantidade de pontos de função com base em uma descrição geral do software e em comparação com outros projetos similares. Essa estimativa pode ser ajustada de acordo com o grau de complexidade do software e outros fatores relevantes.

Assim como na Contagem Indicativa, a estimativa obtida por meio da Contagem Estimativa é apenas uma aproximação do tamanho e complexidade do software a ser desenvolvido, e não substitui a Contagem Detalhada de Pontos de Função, que é realizada posteriormente, com base em informações mais precisas e detalhadas sobre o software a ser desenvolvido.
### Contagem Detalhada (Cd)  
"Contagem Detalhada" (CD) é a técnica principal utilizada na Análise de Pontos de Função (APF) para obter uma contagem precisa do tamanho e complexidade do software a ser desenvolvido.

A Contagem Detalhada envolve a análise detalhada dos requisitos e funcionalidades do software, com o objetivo de identificar todas as funcionalidades que devem ser contadas como pontos de função, bem como sua complexidade. Essa análise é realizada em uma ou mais etapas, dependendo da complexidade do software e da disponibilidade de informações.

Durante a Contagem Detalhada, o analista de pontos de função utiliza um conjunto de regras e diretrizes estabelecidas pelo International Function Point Users Group (IFPUG) ou outras organizações reconhecidas para determinar a quantidade de pontos de função em cada funcionalidade. Essas regras levam em consideração fatores como o número de inputs, outputs, consultas, arquivos e interfaces do sistema, bem como sua complexidade.

A Contagem Detalhada é considerada a técnica mais precisa para medir o tamanho e complexidade do software a ser desenvolvido e é amplamente utilizada em projetos de software para estimar o esforço de desenvolvimento, planejar o cronograma do projeto, alocar recursos e monitorar o desempenho do projeto.

A contagem Detalhada (Cd) analisa todas as funções da dados (ALI’s e AIE’s) classificando com complexidades baixa, média e alta. Também analisa todas as transações classificando sua complexidade em baixa, média e alta conforme tabela de contribuições.

| Funções | Baixa | Média | Alta |
|------------|-----------|-----------|---------|
| ALI     | 7     | 10    | 15   |
| AIE     | 5     | 7     | 10   |
| EE      | 3     | 4     | 6    |
| CE      | 3     | 4     | 6    |
| SE      | 4     | 5     | 7    |  

A seguir temos as tabelas de complexidade para ALI e AIE.

|    | < 20 | 20 – 50 | > 50 |
|------|------|---------|------|
| 1    | Baixa| Baixa   | Média|
| 2 - 5| Baixa| Média   | Alta |
| > 5  | Média| Alta    | Alta |

A seguir temos as tabelas de complexidade para EE.  

|  | < 5 | 5 – 15 | > 15 |
|------|-----|--------|------|
|  < 2  | Baixa| Baixa | Média|
|  2  | Baixa| Média | Alta |
| > 2  | Média| Alta  | Alta |  

A seguir temos as tabelas de complexidade para CE e SE.  

|    | < 6 | 6 – 19 | > 19 |
|------|-----|--------|------|
| < 2  | Baixa| Baixa | Média|
| 2 - 3| Baixa| Média | Alta |
| > 3  | Média| Alta  | Alta |  

Análise Detalhada

|  Descrição  |  Tipo  |  DER  |  RLR  |  Complexidade  |  Contribuição  |
|--------|------|--------------|----|-----|-----|
| ALI Usuário |  ALI  |  4  |  1  |  Baixa  |  7  |  
| ALI Produto |  ALI  |  4  |  1  |  Baixa  |  7  | 
| ALI Estoque |  ALI  |  4  |  1  |  Baixa  |  7  | 
| ALI Cliente |  ALI  |  4  |  1  |  Baixa  |  7  | 
| ALI Venda |  ALI  |  4  |  1  |  Baixa  |  7  | 
|  **Descrição**  |  **Tipo**  |  **DER**  |  **RLR**  |  **Complexidade**  |  **Contribuição**  |  
|  Cadastrar Usuário  |  EE  |  4  |  1  |  Baixa  |  3  |  
|  Alterar Usuário  |  EE  |  4  |  1  |  Baixa  |  3  |  
|  Consultar Usuário  |  CE  |  4  |  1  |  Baixa  |  3  |  
|  Visualizar detalhes do Usuário  |  CE  |  3  |  1  |  Baixa  |  3  |  
|  Excluir Usuário  |  EE  |  2  |  1  |  Baixa  |  3  | 
|  Cadastrar Produto  |  EE  |  4  |  1  |  Baixa  |  3  |  
|  Alterar Produto  |  EE  |  4  |  1  |  Baixa  |  3  |  
|  Consultar Produtos  |  CE  |  4  |  1  |  Baixa  |  3  |  
|  Visualizar detalhes do Produto  |  CE  |  3  |  1  |  Baixa  |  3  |  
|  Excluir Produto  |  EE  |  2  |  1  |  Baixa  |  3  | 
|  Cadastrar Estoque  |  EE  |  4  |  1  |  Baixa  |  3  |  
|  Alterar Estoque  |  EE  |  4  |  1  |  Baixa  |  3  |  
|  Consultar Estoques  |  CE  |  4  |  1  |  Baixa  |  3  |  
|  Visualizar detalhes do Estoque  |  CE  |  3  |  1  |  Baixa  |  3  |  
|  Excluir Estoque  |  EE  |  2  |  1  |  Baixa  |  3  | 
|  Cadastrar Cliente  |  EE  |  4  |  1  |  Baixa  |  3  |  
|  Alterar Cliente  |  EE  |  4  |  1  |  Baixa  |  3  |  
|  Listar Clientes  |  CE  |  4  |  1  |  Baixa  |  3  |  
|  Visualizar detalhes do Cliente  |  CE  |  3  |  1  |  Baixa  |  3  |  
|  Excluir Cliente  |  EE  |  2  |  1  |  Baixa  |  3  | 
|  Incluir Venda  |  EE  |  4  |  1  |  Baixa  |  3  |  
|  Alterar Venda  |  EE  |  4  |  1  |  Baixa  |  3  |  
|  Listar Vendas  |  CE  |  4  |  1  |  Baixa  |  3  |  
|  Visualizar detalhes do Venda  |  CE  |  3  |  1  |  Baixa  |  3  |  
|  Excluir Venda  |  EE  |  2  |  1  |  Baixa  |  3  | 
|  **Total**  |    |    |    |    | **110** |
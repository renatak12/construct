# Relatório de Testes de Módulo/Sistema

# Construct
Responsabilidade do Testador



Criado a partir de: [Processo BSI - Relatório de Testes de Módulo/Sistema](https://docs.google.com/document/d/11hLKf0FcspQrDRfo3gRMXzuY1028cUeniv_Aob8DX_0/edit)

```txt
Legenda

Teste: Código ou identificação do Teste.

Descrição: Descrição dos passos e detalhes do teste a ser executado.

Especificação: Informações sobre a função testada e se ela de acordo com a especificação do caso de uso.

Resultado: Resultado do teste, modificações sugeridas ou resultados do teste. No caso de erro ou problema na execução do teste descrever o erro em detalhes e adicionar print's das telas.
```

## Descrição

Neste documento é abordado os relatórios de Testes de Módulo/Sistema sobre responsabilidade do Testador da iteração.

## Histórico de revisões

| Data       | Versão | Descrição                | Autor                    |
| ---------- | ------ | ------------------------ | ------------------------ |
| 18/05/2023 | 1.0    | Documento Inicial        | Renata Karla Araújo dos Santos  |
| 18/05/2023 | 2.0    | Atualização do Documento | Renata Karla Araújo dos Santos |
| 15/06/2023 | 3.0    | Atualização do Documento | Renata Karla Araújo dos Santos |

### US01 - Manter Funcionario 

| Teste      |      Descrição      |        Especificação          | Resultado            |
| :--------- | :-----------------: | :---------------------------: | :------------------- |
| Teste 01: test_login_view | A1 -Logar usuario A1.1. O sistema executa o login A1.2. O sistema verifica se foi realizado A1.3. Fim do fluxo. | Especificação ok.| Ok. |
| Teste 02: test_cadastro_funcionario_gerente | A1 - Cadastrar funcionario gerente A1.1. O sistema executa o fluxo de usuarios A1.2. O sistema executa a função verifica e retorna A1.3. Fim do fluxo.| Especificação ok.| Ok. |
| Teste 03: test_cadastro_funcionario_vendedor | A1 - Cadastrar funcionario vendedor A1.1. O sistema executa o fluxo de usuarios A1.2. O sistema executa a função verifica e retorna A1.3. Fim do fluxo. | Especificação ok.| Ok. |

### US02 - Manter Produto

| Teste      |      Descrição      |        Especificação          | Resultado            |
| :--------- | :-----------------: | :---------------------------: | :------------------- |
| Teste 01: test_cadastrar_produto | A1 - Cadastrar produto A1.1. O sistema executa o fluxo de vendas A1.2. O sistema executa a função verifica e retorna A1.3. Fim do fluxo. | Especificação ok.| Ok. |

### US03 - Manter Estoque 


### US04 - Manter Cliente

| Teste      |      Descrição      |        Especificação          | Resultado            |
| :--------- | :-----------------: | :---------------------------: | :------------------- |
| Teste 01: test_cadastrar_cliente_get | A1 - Cadastrar cliente A1.1. O sistema executa o fluxo de usuarios A1.2. O sistema executa a função verifica e retorna A1.3. Fim do fluxo. | Especificação ok.| Ok. |

### US05 - Manter Venda

| Teste      |      Descrição      |        Especificação          | Resultado            |
| :--------- | :-----------------: | :---------------------------: | :------------------- |
| Teste 01: test_cadastrar_categoria | A1 - Cadastrar categoria A1.1. O sistema executa o fluxo de venda A1.2. O sistema executa a função verifica e retorna A1.3. Fim do fluxo. | Especificação ok.| Ok. |

### US06 - Manter Fornecedor

| Teste      |      Descrição      |        Especificação          | Resultado            |
| :--------- | :-----------------: | :---------------------------: | :------------------- |
| Teste 01: test_cadastrar_fornecedor_get | A1 - Cadastrar fornecedor A1.1. O sistema executa o fluxo de usuarios A1.2. O sistema executa a função verifica e retorna A1.3. Fim do fluxo. | Especificação ok.| Ok. |


## Relatório de Bugs e Providências

Responsabilidade do Gerente

|      Teste        |           Providência            |        Tarefas/tipo            |
| :---------------- | :------------------------------: | :----------------------------- |
| Teste 01: test_funcionario_str | Corrigir a erro no arquivo models.py na definição de função de Funcionario(models.Model), detectada ao executar os testes do sistema. | Tarefa: Bug de Implementação. |
| Teste 01: test_deletar_cliente | Corrigir a erro no arquivo usuarios.views.py na definição de função de deletar_cliente, detectada ao executar os testes do sistema. | Tarefa: Bug de Implementação. |


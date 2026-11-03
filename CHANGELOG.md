# Histórico de alterações — Atualizador de Produção

Este arquivo registra as funcionalidades, melhorias, correções e testes anotados durante o desenvolvimento.

[Voltar ao README](README.md)

---

## Em desenvolvimento — Outubro de 2026

### Adicionado

- **27/10/2026:** campo **Complemento** na aba Finalizar.
- **28/10/2026:** aba **Comentários** para inclusão de complemento e previsão.

### Corrigido

- **29/10/2026:** ajustado o envio do campo Previsão como data para a tabela Pedidos.
- **27/10/2026:** corrigido o método `validacao_update`, no arquivo `Conexao.py`, para buscar o valor pela coluna indicada no registro, em vez de depender da ordem dos valores no dicionário.
- **29/10/2026:** Corrigido o registro de log, onde na coluna `LogSQL` era enviado o `SELECT` ao invés do `UPDATE` gerado no finalizar.

**Antes:**

```python
# validacao_update do arquivo Conexao.py
valores.append(list(dic_valores.values())[i])

# lista_valores do arquivo log_usuario.py
list_valores = [self.banco['banco'] ,self.valores['item'],data_log,usuario,lista_select['count_row'],lista_select['sql_gerado']]

```

**Depois:**

```python
# validacao_update do arquivo Conexao.py
valores.append(dic_valores[registro['col_change'][i]])

#lista_valores do arquivo log_usuario.py
sql = gtsql.gerador_sql(self.banco)
lista_select = Conexao.atualiza_banco('select',self.banco,str(self.valores['item']))
list_valores = [self.banco['banco'] ,self.valores['item'],data_log,usuario,lista_select['count_row'],sql.retorna_sql_update()]
```

O valor passa a ser recuperado pelo nome da coluna indicado em `registro['col_change'][i]`, reduzindo a dependência da ordem dos valores no dicionário.

### Pendências

- [ ] Validar os bancos e as colunas disponíveis para a aba Comentários.
- [X] Corrigir o log para registrar o comando `UPDATE` efetivamente executado, em vez do comando `SELECT`. **2026-10-29**
- [ ] Testar a função de cancelamento de itens finalizados.
- [ ] Atualizar e validar o executável.

---

## Versão 5 — Alteração de estado

**Período:** julho de 2023

### Adicionado

- **19/07/2023:** criada a interface para alteração de estado.
- **19/07/2023:** o campo de seleção passou a buscar os estados disponíveis conforme o banco escolhido.
- **21/07/2023:** implementada a atualização do estado no banco de dados.

---

## Versão 4 — Preparação para lançamento e acompanhamento

**Período:** julho de 2023  
**Situação:** em andamento

### Adicionado

- **14/07/2023:** recurso para finalizar itens componentes.
- **17/07/2023:** exibição dos cinco registros mais recentes do usuário ao abrir o programa.
- **18/07/2023:** inclusão das interfaces gráficas nas abas para seleção das opções.

### Melhorado

- Organização do código para facilitar futuras implementações.

### Pendente

- [ ] Melhorar a visualização do histórico de registros do usuário.

---

## Versão 3 — BETA para testes com usuários

**Concluída em 17/02/2022**

### Adicionado

- Identificação do usuário por meio de `log_usuario.py`.
- Tabela `log_usuario` no PostgreSQL para armazenar logs de finalização.
- Geração de executável utilizando PyInstaller.
- Armazenamento dos registros enviados para finalização.
- Geração dos comandos `INSERT` a partir da lista de registros.

### Em validação

- Tratamento de casos em que mais de uma chave é encontrada para a ordem informada. **A correção foi registrada, mas o teste não foi confirmado.**

### Melhoria posterior

- O valor do campo `combobox_banco` foi alterado de `Laser` para `plan_laser`.

---

## Versão 2 — Preparação para usuários

**Concluída em 04/02/2022**

### Adicionado e corrigido

- **25/01/2022:** botão para cancelar itens finalizados.
- **26/01/2022:** opção de máquina para o banco Laser.
- Mensagem de sucesso após a finalização.
- Mensagem quando o item não é encontrado.
- Regra para finalizar apenas itens em montagem no banco Pedidos.
- Ajustes nos testes do botão Cancelar e implementação das validações solicitadas.
- Correção para impedir o envio de máquina em branco ao banco Laser.

---

## Versão 1 — Implementação inicial

### Adicionado

- Janela para finalizar itens.
- Opções para os bancos Pedidos e Laser.
- Exibição dos itens finalizados enquanto o programa permanece em execução.
- Comunicação direta com o banco de dados por meio de `Conexao.py`.

---

## Histórico de testes e correções

| Data | Registro |
|---|---|
| **25/01/2022** | Corrigida e testada a geração de atualizações dos itens para o banco Laser. |
| **27/01/2022** | Realizados novos testes e corrigidos erros de validação. |
| **01/02/2022** | Testadas as funções da versão inicial 2.0 para o banco Pedidos; elaborado o fluxograma da função Finalizar. |
| **02/02/2022** | Testadas as funções implementadas para o banco `plan_laser`. |
| **03/02/2022** | Ajustado e testado o funcionamento do botão Cancelar para o banco Pedidos. |
| **27/10/2026** | Corrigido o método `validacao_update` em `Conexao.py`. |

---

## Legenda

- **Adicionado:** nova funcionalidade registrada.
- **Melhorado:** aprimoramento de funcionalidade ou estrutura.
- **Corrigido:** correção registrada.
- **Testado:** teste realizado conforme o histórico.
- **Em validação:** alteração sem confirmação de teste concluído.
- **Pendente:** tarefa ainda não concluída.

---

*As datas e situações refletem as anotações disponíveis no histórico do projeto. Itens sem confirmação de teste foram identificados como tal.*

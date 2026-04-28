# Explicação de Debug do Código debug.py

Este arquivo documenta os erros encontrados no script `debug.py` e descreve as correções aplicadas.

## Erros identificados

1. `input(Preço do item 1? )` sem aspas
   - Erro: sintaxe inválida em Python porque a string não estava delimitada.
   - Correção: `input("Preço do item 1? ")`

2. Conversão de desconto inválida
   - Erro: `desconto_cupom` era lido como string, mas em seguida usado em operação aritmética com números.
   - Correção: converter para `float` na leitura: `desconto_cupom = float(input(...))`

3. Falta de indentação no bloco `if desconto_cupom > 0:` 
   - Erro: o `print` dentro do `if` não estava indentado, o que gera `IndentationError`.
   - Correção: adicionar indentação de 4 espaços antes de `print(...)`.

4. Uso de string normal em `print(" Item 2:        R$ {total_item2:.2f}")`
   - Erro: não era uma f-string, então o placeholder não era substituído pelo valor.
   - Correção: trocar para `print(f" Item 2:        R$ {total_item2:.2f}")`

5. Uso de `round(total, 2)` dentro de f-string com formato `:.2f`
   - Erro: redundância desnecessária. Embora não gere erro, é melhor manter a formatação simples.
   - Correção: usar apenas `print(f" TOTAL:         R$ {total:.2f}")`

## Correções aplicadas no arquivo `debug.py`

- Corrigida a entrada de dados para `item1` adicionando aspas em torno do prompt.
- Convertido `desconto_cupom` para `float` assim que é lido.
- Corrigido o bloco condicional do desconto com indentação adequada.
- Ajustado o `print` do item 2 para usar f-string correta.
- Simplificada a impressão do total final.

## Resultado do código corrigido

O código agora lê corretamente os valores do cliente e dos itens, calcula subtotal, imposto, desconto e total final, e imprime um resumo formatado.

### Trecho de código corrigido
```python
item1 = float(input("Preço do item 1? "))
...
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
...
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
...
print(f" TOTAL:         R$ {total:.2f}")
```

## Observações adicionais

- Se o usuário digitar valores não numéricos para quantidade ou preço, o programa ainda vai gerar `ValueError`.
- Para uma versão mais robusta, recomenda-se adicionar validação das entradas com tratamento de exceções (`try/except`).

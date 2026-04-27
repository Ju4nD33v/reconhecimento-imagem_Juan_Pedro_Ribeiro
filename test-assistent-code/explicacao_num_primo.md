# Explicação Linha a Linha - Verificador de Números Primos

## O que é um número primo?
Um número primo é um número natural maior que 1 que possui apenas dois divisores: 1 e ele mesmo. Exemplos: 2, 3, 5, 7, 11, 13...

---

## Análise do Código

### Linha 1: Definição da Função
```python
def eh_primo(numero):
```
- **`def`**: Palavra-chave para definir uma função em Python
- **`eh_primo`**: Nome da função
- **`numero`**: Parâmetro de entrada (o número que será verificado)

### Linhas 2-8: Docstring (Documentação)
```python
    """
    Verifica se um número é primo.
    
    Args:
        numero (int): O número a ser verificado
        
    Returns:
        bool: True se o número é primo, False caso contrário
    """
```
- **Docstring**: Texto entre `"""` que documenta a função
- Explica o que a função faz
- **Args**: Descreve os parâmetros de entrada
- **Returns**: Descreve o tipo e valor retornado

### Linhas 9-10: Primeiro Tratamento de Caso
```python
    # Números menores que 2 não são primos
    if numero < 2:
```
- **`#`**: Indica um comentário (não é executado)
- **`if numero < 2:`**: Se o número for menor que 2
- **Lógica**: Números como -5, 0 e 1 não são primos por definição

### Linha 11: Retorno para Números Menores que 2
```python
        return False
```
- **`return`**: Encerra a função e retorna um valor
- **`False`**: Valor booleano indicando que o número NÃO é primo
- **Indentação**: 2 níveis (8 espaços) - está dentro do `if`

### Linhas 13-14: Caso Especial do Número 2
```python
    # 2 é o único número primo par
    if numero == 2:
```
- **`==`**: Operador de comparação (igual a)
- **Lógica**: 2 é o único número par que é primo
- **Por que?**: 2 só é divisível por 1 e 2

### Linha 15: Retorno para o Número 2
```python
        return True
```
- **`True`**: Valor booleano indicando que 2 É primo
- **Fluxo**: Se o número for 2, a função encerra aqui e retorna `True`

### Linhas 17-18: Descarte de Números Pares
```python
    # Números pares maiores que 2 não são primos
    if numero % 2 == 0:
```
- **`%`**: Operador módulo (calcula o resto da divisão)
- **`numero % 2 == 0`**: Verifica se há resto zero ao dividir por 2 (se é par)
- **Lógica**: Todo número par > 2 é divisível por 2, logo não é primo

### Linha 19: Retorno para Números Pares
```python
        return False
```
- Se o número é par (e não é 2), não é primo, retorna `False`

### Linhas 21-26: Loop para Verificação de Divisibilidade
```python
    # Verifica divisibilidade por números ímpares até a raiz quadrada
    # Se um número n tem um divisor maior que √n, 
    # ele também tem um divisor menor que √n
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
```

**Detalhamento:**
- **`for i in range(...)`**: Loop que itera sobre valores
  - **`range(3, int(numero ** 0.5) + 1, 2)`**: Gera números começando de 3 até a raiz quadrada de `numero`, incrementando de 2 em 2
  - **`3`**: Início (começa do 3, pois já testamos 2)
  - **`numero ** 0.5`**: Calcula a raiz quadrada (ex: 25 ** 0.5 = 5)
  - **`int(...)`**: Converte para número inteiro
  - **`+ 1`**: Adiciona 1 para incluir o valor da raiz quadrada
  - **`2`**: Incremento (pula números pares, testa apenas ímpares)

- **Exemplo**: Se `numero = 25`
  - `√25 = 5`
  - Range: 3, 5
  - Testa: 25 % 3 e 25 % 5
  - 25 % 5 = 0, então retorna `False` (25 não é primo)

- **`if numero % i == 0:`**: Se encontrou um divisor
- **`return False`**: O número NÃO é primo, encerra a função

### Linha 29: Retorno Final
```python
    return True
```
- Se nenhum divisor foi encontrado até aqui, o número É primo
- Retorna `True`

---

## Exemplos de Uso

### Linhas 32-42: Bloco Principal
```python
# Exemplos de uso
if __name__ == "__main__":
    # Testando alguns números
    numeros_teste = [2, 3, 4, 5, 10, 17, 20, 29, 30, 97]
    
    for num in numeros_teste:
        resultado = eh_primo(num)
        print(f"{num} é primo? {resultado}")
```

- **`if __name__ == "__main__":`**: Esta seção executa apenas quando o arquivo é rodado diretamente (não quando importado)
- **`numeros_teste = [...]`**: Lista com números para testar
- **`for num in numeros_teste:`**: Loop que itera cada número da lista
- **`resultado = eh_primo(num)`**: Chama a função e armazena o resultado
- **`print(f"{num} é primo? {resultado}")`**: 
  - **f-string**: String formatada com `f` no início
  - **`{num}`** e **`{resultado}`**: Variáveis inseridas na string

### Saída Esperada:
```
2 é primo? True
3 é primo? True
4 é primo? False
5 é primo? True
10 é primo? False
17 é primo? True
20 é primo? False
29 é primo? True
30 é primo? False
97 é primo? True
```

---

## Eficiência do Algoritmo

**Por que verificar apenas até √n?**
- Se um número n tem um divisor d > √n, ele também tem um divisor n/d < √n
- Exemplo: 24 = 4 × 6
  - Se 6 > √24 ≈ 4.9, então 4 < √24
  - Só precisamos testar até √24

**Complexidade:**
- Tempo: O(√n) - muito mais rápido que testar todos os números até n
- Espaço: O(1) - usa pouquíssima memória

---

## Fluxograma da Função

```
Entrada: numero
    ↓
número < 2? → SIM → return False
    ↓ NÃO
número == 2? → SIM → return True
    ↓ NÃO
número é par? → SIM → return False
    ↓ NÃO
Testar divisibilidade por [3, 5, 7, ..., √numero]
    ↓
Encontrou divisor? → SIM → return False
    ↓ NÃO
return True (é primo!)
```

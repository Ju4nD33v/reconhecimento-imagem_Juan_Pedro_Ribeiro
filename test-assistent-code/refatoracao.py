def calcular_estatisticas(numeros):
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numeros (list): Lista de números para calcular estatísticas
        
    Returns:
        tuple: (total, media, maximo, minimo) ou (0, 0, None, None) se lista vazia
    """
    if not numeros:
        return 0, 0, None, None
    
    total = sum(numeros)
    media = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    
    return total, media, maximo, minimo


# Exemplo de uso
lista_teste = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, media, maior, menor = calcular_estatisticas(lista_teste)

print(f"Total: {total}")
print(f"Média: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
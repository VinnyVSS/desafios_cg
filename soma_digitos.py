def soma_digitos(n):
    if n < 10:
        return n  # Caso base: número com um único dígito
    return (n % 10) + soma_digitos(n // 10)  # Soma o último dígito e chama recursivamente

numero = int(input("Digite um número inteiro: "))
print(f"Soma dos dígitos: {soma_digitos(numero)}")

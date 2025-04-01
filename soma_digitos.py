def soma_digitos(n):
    if n < 10:
        return n 
    return (n % 10) + soma_digitos(n // 10)  

numero = int(input("Digite um número inteiro: "))
print(f"Soma dos dígitos: {soma_digitos(numero)}")

def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")  # Remove espaços e deixa tudo minúsculo
    return palavra == palavra[::-1]  # Compara com a string invertida

palavra = input("Digite uma palavra: ")
if eh_palindromo(palavra):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")

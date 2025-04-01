def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")  
    return palavra == palavra[::-1] 
palavra = input("Digite uma palavra: ")
if eh_palindromo(palavra):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")

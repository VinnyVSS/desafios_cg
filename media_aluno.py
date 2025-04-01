notas = [float(input(f"Digite a {i+1}ª nota: ")) for i in range(3)]
media = sum(notas) / len(notas)

print(f"Média: {media:.2f}")
if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado.")

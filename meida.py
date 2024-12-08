print("Vamos calcular a sua média!")
nota = float(input("Qual é a sua nota da primeira prova? "))
nota2 = float(input("Qual é a sua nota da segunda prova? "))
resultado = nota + (nota2 * 2)
media = resultado / 3
print(f"A nota da sua primeira prova foi {nota}, a nota da sua segunda prova foi {nota2} e a sua média foi {media:}")
if media >= 5:
    print("Você está aprovado!")
else:
    print("Você está reprovado!")

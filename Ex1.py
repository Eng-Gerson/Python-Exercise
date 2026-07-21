while True:
	nota1 = float(input("Insira a 1ª nota "))
	if nota1 >= 0 and nota1 <= 20:
		break
	print('Nota Inválida')
while True:
	nota2 = float(input("Insira a 2ª nota "))
	if nota2 >= 0 and nota2 <= 20:
		break
	print('Nota Inválida')
media = (nota1+nota2)/2
if media < 10:
	print("Reprovado")
elif media >= 10 and media < 14:
	print("Aprovado")
else: 
	print("Dispensado")
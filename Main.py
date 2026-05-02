def Ex1():
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

def Ex2():
	Num = [[]] * 3
	for i in range(3):
		Num[i] = int(input(f"Insira o {i+1}º número"))
	Num.sort()
	print(f"O maior deles é {Num[2]}")

def Ex3():
	Number = [[]] * 3
	for i in range(3):
		Number[i] = int(input(f"Insira o {i+1}º número"))
	Number.sort()
	print(f"O menor número é: {Number[0]} \nO maior número é: {Number[2]}")

def Ex4():
	i = int(input("i = "))
	j = int(input("j = "))
	i,j = j,i
	print(f"Realizando a troca \ni = {i}")
	print(f"j = {j}")

def Ex5():
	Num = [[]] * 3
	for i in range(3):
		Num[i] = int(input(f"Insira o {i+1}º número "))
	Num.sort()
	Num.reverse()
	print(Num)

def Ex6():
	escolha = input("Qual é o seu turno?\nM-Matutino\nV-Vespertino\nN-Nocturno\nR:")
	if escolha is 'M':
		print("Bom dia!")
	elif escolha is 'V':
		print('Boa tarde!')
	elif escolha is "N":
		print("Boa noite!")
	else:
		print("Valor inválido")

def Ex7():
	while True:
		salario = float(input("Insira o salário "))
		if salario >= 0:
			break
		print("É para inserir salário e não dívida,insira um valor positivo")
	print(f"Antes do reajuste o salário é {salario}")
	if salario <= 5000:
		percentual = 0.2
		salario += salario * percentual
	elif salario < 12000:
		percentual = 0.15
		salario += salario * percentual
	elif salario < 25000:
		percentual = 0.1
		salario += salario * percentual
	else:
		percentual  = 0.05
		salario += salario * percentual
	print(f"O percentual do aumento é {percentual*100}% \nO valor do aumento é {round((percentual*salario)/(1+percentual),5)}\nNovo salário após o reajuste é {round(salario,5)}")

#def Ex8():
	
def Palindromo():
	string = input("Insira uma string ")
	string.lower()
	String = string[::-1]
	if string == String:
		print("É palindromo")
	else:
		print("Não é palindromo")

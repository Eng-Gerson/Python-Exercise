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

def Ex21():
	Num = []
	for i in range(3):
		Num.append(int(input(f"Insira o {i+1}º número ")))
	print(f"O maior número é {max(Num)}")

def Ex3():
	Number = [[]] * 3
	for i in range(3):
		Number[i] = int(input(f"Insira o {i+1}º número"))
	Number.sort()
	print(f"O menor número é: {Number[0]} \nO maior número é: {Number[2]}")

def Ex31():
	Num = []
	for i in range(3):
		Num.append(int(input(f"Insira o {i+1}º número ")))
	print(f"O menor número é {min(Num)} e o maior número é {max(Num)}")

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
	if escolha == 'M':
		print("Bom dia!")
	elif escolha == 'V':
		print('Boa tarde!')
	elif escolha == "N":
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
	salario_antes = salario
	if salario <= 5000:
		percentual = 0.2
	elif salario < 12000:
		percentual = 0.15
	elif salario < 25000:
		percentual = 0.1
	else:
		percentual  = 0.05
	salario += salario * percentual
	print(f"O percentual do aumento é {percentual*100}% \nO valor do aumento é {round((salario - salario_antes),5)}\nNovo salário após o reajuste é {round(salario,5)}")

def Ex8():
	Resposta =[[]] * 5
	Resposta[0] = input("Telefonou para vítima? ")
	Resposta[1] = input("Esteve no local do crime? ")
	Resposta[2] = input("Mora perto da vítima? ")
	Resposta[3] = input("Devia para a vítima? ")
	Resposta[4] = input("Já trabalhou com a vítima? ")
	contador = 0
	for i in range(5):
		Resposta[i] = Resposta[i].lower()
		if Resposta[i] == "sim" or Resposta[i] == "s" or Resposta[i] == "y" or Resposta[i] == "yes" or Resposta[i] == "si" or Resposta[i] == "oui":
			contador = contador + 1
	if contador == 2:
		print("Suspeito")
	elif contador == 3 or contador == 4:
		print("Cúmplice")
	elif contador == 5:
		print("Assasino")
	else:
		print("Inocente")
	
def Palindromo():
	string = (input("Insira uma string ")).lower()
	if string[0::] == string[::-1]:
		print("É palindromo")
	else:
		print("Não é palindromo")
def Collatz():
	while True:
		a = int(input("Insira um inteiro positivo "))
		while a != 1 :
			if a % 2 == 0:
				a = a/2
			else:
				a = 3*a + 1
			print(a)
		n = int(input("1 \nVai inserir outro número? \n1-Sim \n2-Não \nR: "))
		if n == 2:
			break
	
		

#lados e classificacao de triangulo
#Pretende-se mostrar o valor da area de uma entre as duas figuras geometricas triangulo ou rectangulo.
#faca um programa que pela escolha do usuario mostra na saida o valor da area;
#Faca um programa que frecebe por teclado um numero e informa se o numero e divisivel por sete e 8
def Tarefa1():
	a = float(input("Insira o tamanho do primeiro lado "))
	b = float(input("Insira o tamanho do segundo lado "))
	c = float(input("Insira o tamanho do terceiro lado "))
	if(a == b == c):
		print("O triangulo é equilatero")
	elif(a != b != c):
		print("O triangulo é escaleno")
	else:
		print("O triangulo é isoceles")

def Tarefa2():
	escolha = int(input("Qual figura vai querer calcular a area? \n1-Triangulo \n2-Rectangulo \nOutro - Sair"))
	if escolha == 1:
		base = float(input("Insira o valor da base "))
		altura = float(input("Insira o valor da altura "))
		print(f"A area do triangulo é {base*altura/2}")
	elif escolha == 2:
		lado1 = float(input("Insira o valor do comprimento "))
		lado2 = float(input("Insira o valor da largura "))
		print(f"A area do rectangulo é {lado1*lado2}")
	else:
		print("Obrigado!")

def Tarefa3():
	num = int(input("Insira um número "))
	if num % 7 == 0 and num % 8 == 0:
		print(f"O número {num} é divisível por 7 e 8")
	else:
		print(f"O número {num} não é divisível por 7 e 8")		
		
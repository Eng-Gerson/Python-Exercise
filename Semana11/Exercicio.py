import array as arr
def Ex1():
    for i in range(100):
        print(i+1)

def Ex2():
    for i in range(250,89,-1):
        if i % 4 == 0:
            print(i)

def Ex3():
    soma = 0
    cont = 0
    for i in range(2030,1999,-1):
        print(i)
        soma += i
        if i % 2 == 0:
            cont += 1
    print(f"A soma desses números é {soma} e existem {cont} números pares")

def Ex4():
    soma = 0
    while True:
        num = float(input("Insira um número "))
        if num >= 0:
            soma += num
        else:
            break
    print(f"A soma dos números inseridos é {soma}")

def Ex5():
    notas = arr.array('f',[])
    n = int(input("Quantas notas vai inserir? "))
    for i in range(n):
        while True:
            k = float(input(f"Insira a {i+1}º nota "))
            if k >= 0 and k <= 20:
                break
            print("Essa nota é inválida, insira uma nota válida ")
        notas.append(k)
    print("As notas positivas são:", end= " ")
    for j in notas:
        if j >= 10:
            print(j,end= " ")

def Ex6():
    num = arr.array('f',[])
    soma = 0
    cont = 0
    for i in range(50):
        while True:
            n = float(input("Insira um valor no intervalo de 20 a 60 "))
            if n >= 20 and n <= 60:
                break
            print("O número inserido não pertence a esse intervalo, insira outro número ")
        num.append(n)
    print("Os números armazenados são:",end= " ")
    for j in num:
        print(j,end= " ")
        soma += j
        if j % 3 == 0 or j % 7 == 0:
            cont += 1
    print(f"\nA soma deles é {soma} e {cont} números são múltiplos de 3 ou 7 ")

Ex5()

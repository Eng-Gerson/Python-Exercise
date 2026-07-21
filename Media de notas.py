def Calcular():
    nota = []
    percent = []
    soma,condition = 0,0
    lim = int(input("Quantas notas vai inserir? "))
    for i in range(lim):
        while(True):
            num = float(input(f"Insira a {i+1}ª nota "))
            if 0 <= num <= 20 :
                nota.append(num)
                break
            else:
                print("Valor inválido, insira novamente")

        percent.append(float(input("Insira a percentagem da nota ")))
    if sum(percent) != 1:
        print("A percentagem é inválida ")
    else:
        msg = "Excluído"
        for i in range(lim):
            soma += nota[i] * percent[i]
        soma = round(soma,0)
        for x in nota:
            if x < 10:
                condition += 1
        if 10 <= soma < 14 or condition > 0:
            msg = "Admitido"
        elif soma >= 14:
            msg = "Dispensado"
        print(f"A media = {soma} e o estado = {msg}")


def Estimar():
    print("Ha")
while(True):
    print("---------Media---------")
    op = int(input("Escolha o que fazer \n1-Calcular Média \n2-Estimar para admissão/dispensa \n3-"))
    if(op == 1):
        Calcular()
    elif(op == 2):
        Estimar()
    elif(op == 3):
        print("KKK")


from OOP import Person

def Ler(msg):
    a = input(msg)
    return a

p1 = Person(Ler("Coloque nome "),Ler("Coloque idade "),Ler("Coloque genero "))
print(p1.name)
print(p1.age)
print(p1.gender)
p1.Talk()


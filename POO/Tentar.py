class Tentar:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def Recursivo(self,r):
        if r == 0:
            return 1
        return r * self.Recursivo(r-1)

    def Imprimir(self):
        print(f"{a} é {b} é {c}")

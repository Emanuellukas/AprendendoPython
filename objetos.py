print("porra")
class Cachorro:
    def __init__(self, nome): #Método construtor com 1 argumento
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def latir(self):
        print("está latindo")

    def comer(self):
        print(" agora está comendo")
def main():
    dog = Cachorro()
    dog.latir()
    print(dog.get_nome())

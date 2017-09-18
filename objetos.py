class Carro:
    def __init__(self, tipo = 'Corsa'):
        self.tipo = tipo #Dizendo que o padrão é Corsa e que ele pegará o que vier passado no parâmetro

    def tipoCarro(self):
        return self.tipo

def main():
    carro1 = Carro()
    print(carro1.tipoCarro())
    carro2 = Carro("Ka")
    print(carro2.tipoCarro())
    carro3 = Carro()
    x = carro3.tipoCarro()
    print(x)

if __name__ == "__main__": main()
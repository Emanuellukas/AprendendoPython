def main():
    try:
        arq = open('exemplo.txt')
        for linha in arq: print(linha.strip()) #Uma outra forma de fazer (linha, end='')

    except IOError as erro:
        print("Não encontramos o arquivo: ", erro)

if __name__ == '__main__': main()

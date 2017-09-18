#Dicionário associativo

def main():
    #dicionario = {'um' : 1, 'dois' : 2, 'três' : 3, 'quatro' : 4}
    dicionario = dict(
        nome = 'Lucas', dois = 2, tres = 3, quatro = 'quatroo'
    )

    for key in sorted(dicionario.keys()):
        print(key, dicionario[key]) #imprime o índice e outro valor na mesma posição do índice
        print(dicionario['nome'])




if __name__ == '__main__': main()

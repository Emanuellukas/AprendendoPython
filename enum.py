def main():
    arq = open('exemplo.txt')
    for index, linha in enumerate(arq.readlines()): #index é o índice do Enumerate
        print(index, linha, end='')

    s = "esse e meu texto"
    for i, str in enumerate(s):
        print(i, str, end=' \n',)

if __name__ == '__main__': main ()

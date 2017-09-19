def main():
    s = "esse é meu texto"
    for c in s:
        if c == 'm': continue #Faz com que o loop ignore a letra selecionada
        if c == 'x': break #Faz com que o loop se encerre assim que encontrar a letra selecionada
        print(c, end='')

if __name__ == '__main__': main()

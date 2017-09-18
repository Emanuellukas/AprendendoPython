def main():
    x, y = 2, 1
    resultado = "menor que" if x < y else "maior que"
    print(resultado)

    #Ou

    if x < y:
        print("X é menor que Y!")
    elif x > y:
        print("X é maior que Y!")
    else:
        print("X e Y têm valores iguais!")

if __name__ == "__main__": main()
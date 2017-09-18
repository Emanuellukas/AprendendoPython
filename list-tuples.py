def main():
    x = (1, 2, 3)
    y = [23, 14, 9, 4]
    y.append(10)
    print(type(x), x)
    print(type(y), y)

    y.insert(4, "oi") #Insere o segundo parâmentro logo após o índice escolhido no primeiro parâmetro
    print(type(y[2]), y) #Diz o tipo de dado na posição do índice 2
    print(type(y[4]), y) #Diz o tipo de dado na posição do índice 2

    for i in y:
        print(i)

if __name__ == '__main__': main()

'''Do ponto de vista técnico em Python uma tupla é imutável e uma lista é mutável.'''

'''Do ponto de vista conceitual você deveria usar tuplas para montar estruturas de dados 
heterogêneos enquanto a lista deveria ser usada para dados homogêneos, ou seja,
 todos seus elementos deveriam ser do mesmo tipo.'''
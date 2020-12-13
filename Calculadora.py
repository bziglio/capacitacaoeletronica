def soma():
    num1 = int(input("Digite o seu primeiro número. "))
    num2 = int(input("Digite o seu segundo número. "))
    print('')
    print(num1 + num2)

def subtracao():
    num1 = int(input("Digite o seu primeiro número. "))
    num2 = int(input("Digite o seu segundo número. "))
    print('')
    print(num1 - num2)

def multiplicacao():
    num1 = int(input("Digite o seu primeiro número. "))
    num2 = int(input("Digite o seu segundo número. "))
    print('')
    print(num1*num2)

def divisao():
    num1 = int(input("Digite o seu primeiro número. "))
    num2 = int(input("Digite o seu segundo número. "))
    print('')
    print(num1/num2)

def quadrado():
    num = int(input("Digite o seu número. "))
    print('')
    print(num**2)

def potencia():
    num1 = int(input("Digite o número. "))
    num2 = int(input("Digite a potência. "))
    print('')
    print(num1**num2)

def soma():
    num1 = float(input("Digite o seu primeiro número. "))
    num2 = float(input("Digite o seu segundo número. "))
    print('')
    print(str(num1) + ' + ' + str(num2) + ' = ' + str(num1 + num2))

def subtracao():
    num1 = float(input("Digite o seu primeiro número. "))
    num2 = float(input("Digite o seu segundo número. "))
    print('')
    print(str(num1) + ' - ' + str(num2) + ' = ' + str(num1 - num2))

def multiplicacao():
    num1 = float(input("Digite o seu primeiro número. "))
    num2 = float(input("Digite o seu segundo número. "))
    print('')
    print(str(num1) + ' . ' + str(num2) + ' = ' + str(num1 * num2))

def divisao():
    num1 = float(input("Digite o seu primeiro número. "))
    num2 = float(input("Digite o seu segundo número. "))
    print('')
    print(str(num1) + ' / ' + str(num2) + ' = ' + str(num1 / num2))

def quadrado():
    num = float(input("Digite o seu número. "))
    print('')
    print(str(num) + ' ^2 = ' + str(num ** 2))

def potencia():
    num1 = float(input("Digite o número. "))
    num2 = float(input("Digite a potência. "))
    print('')
    print(str(num1) + ' ^' + str(num2) + ' = ' + str(num1 ** num2))

def raiz_quadrada():
    num = float(input("Digite o número. "))
    print('')
    print(str(num) + ' ^0.5  = ' + str(num ** 0.5))

def raiz():
    num1 = float(input("Digite o número. "))
    num2 = float(input("Digite a raíz. "))
    print('')
    print(str(num1) + ' ^' + str(1/num2) + ' = ' + str(num1 ** (1/num2)))

def fatorial():
    num = int(input("Digite o número. "))
    x = 1
    for i in range(1, num+1):
        x = x*i
    print('')
    print(str(num) + '! = ' + str(x))




if __name__== "__main__":

    operacao = 0
    while operacao != '0':
        print('\n\n0 - Desligar a calculadora \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão')
        print('5 - Quadrado \n6 - Potência \n7 - Raíz Quadrada \n8 - Raíz \n9 - Fatorial \n\n')
        operacao = input('Qual operação quer realizar? ')
        
        if operacao == '1':
            soma()

        elif operacao == '2':
            subtracao()

        elif operacao == '3':
            multiplicacao()

        elif operacao == '4':
            divisao()

        elif operacao == '5':
            quadrado()

        elif operacao == '6':
            potencia()

        elif operacao == '7':
            raiz_quadrada()

        elif operacao == '8':
            raiz()

        elif operacao == '9':
            fatorial()

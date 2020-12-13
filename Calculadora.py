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

def raiz_quadrada():
    num = int(input("Digite o número. "))
    print('')
    print(num**0.5)

def raiz():
    num1 = int(input("Digite o número. "))
    num2 = int(input("Digite a raíz. "))
    print('')
    print(num1**(1/num2))

def fatorial():
    num = int(input("Digite o número. "))
    x = 1
    for i in range(1, num+1):
        x = x*i
    print('')
    print(x)


def funcoes():
    print('')
    print('')
    print('0 - Desligar a calculadora')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Quadrado')
    print('6 - Potência')
    print('7 - Raíz Quadrada')
    print('8 - Raíz')
    print('9 - Fatorial')
    print('')


if __name__== "__main__":

    operacao = 0
    while operacao != '0':
        funcoes()
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

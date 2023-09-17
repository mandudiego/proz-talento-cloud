"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""

def calc(n1, n2, op):
    if op == 1:
        soma = n1 + n2
        return print(f'Soma: {soma}')
    elif op == 2:
        subtracao = n1 - n2
        return print(f'Subtração: {subtracao}')
    elif op == 3:
        multiplicacao = n1 * n2
        return print(f'Multiplicação: {multiplicacao}')
    elif op == 4:
        if n2 == 0:
            return print('Divisão por zero')
        else: 
            divisao = n1 / n2
            return print(f'Divisão: {divisao}')
    else:
        return print('0')

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
op = int(input('[1] SOMA\n[2] SUBTRAÇÃO\n[3] MULTIPLICAÇÃO\n[4] DIVISÃO\nOperação: '))

calc(n1, n2, op)
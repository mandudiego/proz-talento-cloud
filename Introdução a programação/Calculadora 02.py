"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 
"""
def calc(n1, n2, op):
    if op == 1:
        soma = n1 + n2
        return soma 
    elif op == 2:
        subtracao = n1 - n2
        return subtracao
    elif op == 3:
        multiplicacao = n1 * n2
        return multiplicacao
    elif op == 4:
        if n1 == 0 or n2 == 0:
            return None
        else: 
            divisao = n1 / n2
            return divisao

    


while True:
    op = int(input('[1] SOMA\n[2] SUBTRAÇÃO\n[3] MULTIPLICAÇÃO\n[4] DIVISÃO\n[0] SAIR\nOperação: '))
    if op == 0:
        print('Saindo...')
        break
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))

    resultado = calc(n1, n2, op)
    print(f'Resultado: {resultado}')
    print()
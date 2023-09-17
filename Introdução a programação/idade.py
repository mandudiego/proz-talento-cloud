"""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
"""
from datetime import date

anoAtual = date.today().year
nome = input('Digite seu nome completo: ')
while True:  
    anoNascimento = input(f'Em que ano você nasceu? ')
    if not anoNascimento.isdigit():
        print('[Erro] Você deve digitar apenas números')
    elif int(anoNascimento) > anoAtual:
        print('[Erro] Ano nascimento maior que o atual')
    elif int(anoNascimento) < 1922:
        print('[ERRO] Ano inválido.')
    else:
        anoNascimento = int(anoNascimento)
        idade = anoAtual - anoNascimento
        break
print (f'Nome: {nome}\nIdade: {idade}')
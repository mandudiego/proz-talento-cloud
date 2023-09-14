"""
Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
"""

andares = range(1, 21)
andaresDecrescente = range(20, 0, -1)
i = 1
j = 1
for i in andares:
    if i == 13:
        continue
    print(f'{i}º andar')
    
    i += 1

print()

for j in andaresDecrescente:
    if j == 13:
        continue
    print(f'{j}º andar')
    j -= 1
    


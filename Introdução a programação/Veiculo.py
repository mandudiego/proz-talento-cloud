"""
Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg.
"""
print('HABILITAÇÃO')
print('-=' * 15)

quantidadeRodas = int(input('Insira a quantidade de rodas de seu veículo: ')) # Ex: 4
pesoBruto = int(input('Insira o peso bruto de seu veículo: ')) # Ex: 3000kg
quantidadePessoas = int(input('Quantidade de pessoas que seu veículo suporta: ')) # Ex: 4

if quantidadeRodas <= 3:
    print('CNH A')
elif quantidadeRodas == 4 and pesoBruto <= 3500:
    print('CNH B')
elif quantidadeRodas >= 4 and pesoBruto <= 6000:
    print('CNH C')
elif quantidadePessoas > 8:
    print('CNH D')
elif pesoBruto > 6000:
    print('CNH E')
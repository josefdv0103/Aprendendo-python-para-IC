#import random
#print(20*'=-')
#print('VAMOS JOGAR PAR OU ÍMPAR')
#print(20*'=-')
#cont = 0
#while True:
#    n = int(input('Diga um valor: '))
#    e = str(input('Escolha par ou ímpar[P/I]: ')).upper().strip()[0]
#    c = random.randrange(0,11)
#    s = n + c
#    if s % 2 == 0:
#        print(f'Você jogou {n} e o computador {c}. Total de {s} DEU PAR')
#        if e == 'P':
#            print('Você ganhou!')
#        if e == 'I':
#            print('Você perdeu!')
#            break
#    elif s % 2 != 0:
#        print(f'Você jogou {n} e o computador {c}.Total de {s} DEU IMPAR')
#        if e =='I':
#            print('Você ganhou!')
#        if e =='P':
#            print('Você perdeu!')
#            break
#    cont =+ 1
#print(f'GAME OVER! Você venceu {cont} vezes')

#Flag com break
#s = c = 0
#while True:
#    n = int(input('Digite um valor (999 para parar: '))
#    if n == 999:
#        break
#    s += n
#    c += 1
#print(f'A soma dos {c} valores foi {s}!')

#TABUADA
#c = 1
#print('------------------------------------------------')
#n = int(input('Quer ver a tabuada de qual valor? '))
#while True:
#    if c <= 10:
#        m = c*n
#        print(f'{n} x {c} = {m}')
#        c += 1
#    if c >10:
#        n = int(input('Quer ver a tabuada de qual valor? '))
#        c = 1
#        print('------------------------------------------------')
#    if n < 0:
#        break
#
#
#while True:
#    n = int(input('Quer ver a tabuada de qual valor? '))
#    if n < 0:
#        break
#    print('------------------------------------------------')
#    for c in range (1, 11):
#        print(f'{n} x {c} = {n*c}')
#    print('------------------------------------------------')
#print('Tabuada encerrada')


#CADASDRO
#print(20*'-')
#print('CADASTRE UMA PESSOA')
#print(20*'-')
#maior = h = mu = 0
#while True:
#    print(20*'-')
#    i = int(input('Idade: '))
#    s = str(input('Sexo: [M/F] ')).upper().strip()[0]
#    print(20*'-')
#    if i > 18:
#        maior += 1
#    elif s == 'M':
#        h += 1
#    elif s == 'F' and i < 20:
#        mu += 1
#    r = str(input('Quer continuar?')).strip().upper()[0]
#    if r == 'N': 
#        break
#    elif r not in 'Ss':
#        r = str(input('Quer continuar?')).strip().upper()[0]
#print(f'''Total de pessoas com mais de 18 anos: {maior}
#Ao todo temos {h} homens cadastrados
#E temos {mu} mulheres com menos de 20 anos
#''')

#COMPRAS
#print(20*'-')
#print('LOJA SUPER BARATÃO')
#print(20*'-')
#t = s = c = 0
#b = ''
#while True:
#    n = str(input('Nome do Produto: ')).strip()
#    p = float(input('R$ '))
#    s += p
#    r = str(input('Quer continuar? ')).strip().upper()[0]
#    if r in 'Nn':
#        print(20*'-', 'FIM DO PROGRAMA', 20*'-')
#        break
#    elif p > 1000:
#        t += 1
#    elif c == 0:
#        menor = p
#        b = n
#    elif c != 0 and p < menor:
#        menor = p
#        b = n
#    c += 1
#print(f'''Total da compra foi R$ {s:.2f}
#Temos {t} produtos custando mais de R$ 1000,00
#O produto mais barato foi {b} que custa R$ {menor:.2f}''')

from math import floor
print(50*'=')
print('BANCO NU')
print(50*'=')
while True:
    v = int(input('Que valor você quer? '))
    if v / 50 > 0:
        print(f'Total de {floor(v / 50)} cédulas de R$ 50 ')
        v = v - floor((v / 50))*50
    if v >= 20:
        print(f'Total de {floor(v / 20)} cédulas de R$ 20 ')
        v = v - floor((v/20)) * 20
    if v >= 10:
        print(f'Total de {floor(v / 10)} cédulas de R$ 10')
        v = v - floor(v/10)*10
    if v >= 5:
        print(f'Total de {floor(v / 5)} cédulas de R$ 5 ')
        v = v - floor(v/5)*5
    if v >= 1:
        print(f'Total de {v:.0f} células de R$ 1')
    break
print(50*'=')
print('Volte sempre no Banco Nu')

import 

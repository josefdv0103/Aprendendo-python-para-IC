#1
#n = int(input('Digite um número de 0 a 20: '))
#
#while True:
#    i = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
#    if 0 <= n <= 20:
#        print(f'Seu número por extenso é {i[n]}')
#        break
#    else:
#        n = int(input('Digite seu número novamente de 0 a 20: '))

#2
#b = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'Corinthians', 
#'Internacional', 'Fluminense', 'Athletico-PR', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Sao Paulo',
#'Juventude', 'América-MG', 'Santos', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense')
#
#print(b)
#print(20*'=-')
#print(b[0:5])
#print(20*'=-')
#print(sorted(b))
#print(20*'=-')
#i = b.index('Palmeiras')
#print(f'O Palmeiras é o {i + 1}° colocado')
#print(20*'=-')

#3
#import random

#f = (random.randint(0, 10),random.randint(0, 10),random.randint(0, 10),random.randint(0, 10),random.randint(0, 10))
#print(f'Os números sorteados foram: {f[0]} {f[1]} {f[2]} {f[3]} {f[4]}')
#sorted(f)
#print(f'O menor número é: {f[4]}')
#print(f'O maior número é: {f[0]}')

#4
a = int(input('Digite um número: '))
b = int(input('Digite um outro valor: '))
c = int(input('Digite um outro valor: '))
d = int(input('Digite um outro valor: '))

print(f'Você digitou 
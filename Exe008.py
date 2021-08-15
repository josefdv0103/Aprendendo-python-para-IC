#import time
#for x in range(10, -1, -1):
#    print(x)
#    time.sleep(1)
#print('BUM BUM POWW')

#for x in range(0, 51, 2):
#    print(x, end=' ')
#print('Acabou')

#s, i = 0, 0
#for x in range(1, 501, 2):
#    if x % 3 == 0:
#        i += 1
#        s += x
#print('A soma dos {} numeros impares é: {}'.format(i, s))

#y = int(input('Digite um número para ver sua tabuada: '))
#for x in range(1, 11):
#    print(y, 'x', x, ' = ', x*y)

#a = [0, 0, 0, 0, 0, 0]
#s = 0
#for x in range(0, 6):
#    a[x] = int(input('Digite um número: '))
#   if a[x] % 2 == 0:
#       s += a[x]
#print('A soma dos pares é: {}'.format(s))

#print(20*'=', '''\n10 TERMOS DE UMA PA\s''', 20*'=')
#p = int(input('Primeiro termo: '))
#r = int(input('Razão: '))
#s = p
#for x in range(0, 10):
#    print(s, '-> ', end='')
#    s += r
#print('ACABOU')

#c = 0
#x = int(input('Digite um número: '))
#for y in range(1, x+1):
#   if x % y == 0:
#       print('\033[33m', end=' ')
#       c += 1
 #   elif x % y != 0:
#       print('\033[31m', end=' ')
#   print('{}'.format(y), end=' ')
#print('\s\033[mO número {} foi divisível {} vezes'.format(x, c))
#if c == 2:
#    print('E por isso ele é primo')
#if c != 2:
#    print('E por isso ele não é primo')

#f = str(input('Digite uma frase: ')).strip().upper()
#fa = f.split()
#j = ''.join(fa)
#i = j[::-1](opcional)
#i = ''
#for x in range(len(j) - 1, -1, -1):
#    i += j[x]
#print('O inverso de {} é {}'.format(j, i))
#if i == j:
#    print('É um palindromo')
#else:
#   print('Não é um palindromo')
#b, c = 0, 0
#for x in range(1, 8):
#   a = int(input('Em que ano a {}ª pessoa nasceu? '.format(x)))
#    if a > 2000:
#       c += 1
 #   elif a <= 2000:
#      b += 1
#print('''Ao todo tivemos {} pessoas maires de idade
#E também tivemos {} pessoas menores de idade'''.format(b, c))

#maior,  menor = 0, 100000
#for x in range(1, 6):
#   p = float(input(('Peso da {}ª pessoa: '.format(x))))
#   if p > maior:
#       maior = p
 #   elif p < menor:
#       menor = p
#print('O maior peso lido foi de: {.:1f}Kg'.format(maior))
#print('O menor peso lido foi de: {.:1f}Kg'.format(menor))

m = [1, 1, 1, 1]
maior = ['Maior', 1]
f = 0
for x in range(1, 5):
    print(20*'-', '{}ª Pessoa'.format(x), 20*'-')
    n = str(input(('Nome: ')))
    i = int(input('Idade: '))
    s = str(input('Sexo[M,/F]: '))
    m[x-1] = i
    if x == 1 and s in 'Mm':
        maior[1] = i
        maior[0] = n
    if i > maior[1] and s in 'Mm':
        maior[1] = i
        maior[0] = n
    if s in 'Ff' and i < 20:
        f += 1
print('A média de idade do grupo é de {:.2f}'.format(sum(m)/4))
print('O homem mais velho tem {} anos e se chama {}'.format(maior[1], maior[0]))
print('Ao todo são {} mulheres com menos de 20 anos'.format(f))

#s = str(input('Informe seu sexo: ')).strip().upper()[0]

#while s not in 'MmFn':
#   s = str(input('Dados invalidos. Por favor, informa se sexo: ')).strip().upper()[0]
#print('Sexo {} registrado com sucesso'.format(s))

#import random
#n = random.randrange(11)
#print('''Sou seu computador...
#Acabei de pensar em um número entre 0 e 10.
#Será que você consegue adivinhar qual foi?''')
#p = ''
#t = 0
#while p != n:
#    p = int(input('Qual o seu palpite? '))
#    if p > n:
#        print('Menos... Tente mais um vez')
#    elif p < n:
#        print('Mais.. Tente mais um vez')
#    t += 1
#print('Acertou com {} tentativas. Parabés!'.format(t))

#import time
#n = 4
#while n != 5:
#   if n == 4:
#      a = int(input('Primeiro valor: '))
#        b = int(input('Segundo valor: '))
#    print('''[ 1 ] somar
#[ 2 ] multiplicar 
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa''')
#    n = int(input('Qual a sua opção? '))
#    if n == 1:
#        print('A soma entre {} + {} é {}'.format(a, b, a+b))
#    elif n == 2:
#        print('A multiplicação entre {} e {} é {}'.format(a, b, a*b))
#    elif n == 3:
#        if a - b > 0:
#            print('Entre {} e {} o maior valor é {}'.format(a, b, a))
#        if a - b < 0:
#            print('Entre {} e {} o maior valor é {}'.format(a, b, b))
#    elif n == 4:
#        print('Informe os numeros novamente: ')
#    elif n == 5:
#        print('Finalizando...')
#    else:
#        print('Opção inválida. Tente novamente')
#    print(20*'=-')
#time.sleep(2)
#print('Fim do programa! Volte sempre')

# = int(input('Digite um número para calcular o fatorial: '))
#p = n
#f = 1
#print('Calculando {}! = '.format(n), end='')
#while p > 0:
#    print('{}'.format(p), end='')
#    print(' x ' if p > 1 else ' = ', end='')
#    f *= p
#    p -= 1
#print('{}'.format(f))

# 10 primeiros termos de uma PA
#print(20*'-=', 'Gerador de PA', 20*'=-')
#p = int(input('Primeiro termo:'))
#r = int(input('Razão: '))
#x = 10
#s = p
#while x >= 1:
#    print('{} -> '.format(s), end='')
#    s += r
#    x -= 1
#print('FIM')

# Termos de uma PA (quantos eu quiser)
#print(20*'=-','Gerador de PA', 20*'=-')
#p = int(input('Primeiro termo: '))
#r = int(input('Razão: '))
#s = p
#x = 10
#y = 10
#z = 0
#while y != 0:
#    x = y
#    while x > 0:
#        print('{} -> '.format(s), end='')
#        s += r
#        x -= 1
#    print('PAUSA')
#    y = int(input(('quantos termos vcê quer mostar a mais?')))
#    z = z + y
#print('Progressão finalizada com {} termos mostrados'.format(z + 10))

#Fibonacci
#print(20*'-=', '\nSequência de Fibonacci\n', 20*'-=')
#q = int(input(('Quantos termos você quer mostrar?')))
#x = 0
#f1 = 1
#f2 = 1
#s = 0
#while x <= q:
#    if x == 0:
#        print('{} -> '.format(f1-1))
#    elif x == 1:
#        print('{} -> '.format(f1))
#    elif x == 2: 
#        print('{} -> '.format(f1))
#    elif x == 3:
#        s = f1 +  f2
#        f1 = f2
#        print('{} -> '.format(s))
#    else:
#        s = s + f2
#        f2 = s - f2
#        print('{} -> '.format(s))
#    x += 1
#print('FIM')

#Gambiarra do flag
#s = x = n = 0
#x = int(input('Digite um número [999 para parar]: '))
#while x != 999:
#    n += 1
#    s += x
#    x = int(input('Digite um número [999 para parar]: '))
#print('Você digitou {} números e a soma entre eles foi {} '.format(n, s))


#l = ''
#n = s = c = 0
#while l != 'N':
#    n = int(input('Digite um número: '))
#    l = str(input('Quer continuar? [S/N]')).upper().strip()[0]
#    if c == 0:
#        menor = maior = n
#    elif c != 0 and n > maior:
#        maior = n
#    elif c != 0 and n < menor:
#        menor = n
#    s += n
#    c += 1
#m = s/c
#print('''Você digitou {} números e a média foi {}
#O maior valor foi {} e o menor foi {}'''.format(c, m, maior, menor))


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

import time
n = ''
while n != 5:
    if n not in (1, 2, 3, 5):
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
    print('''[ 1 ] somar
[ 2 ] multiplicar 
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    n = int(input('Qual a sua opção? '))
    if n == 1:
        print('A soma entre {} + {} é {}'.format(a, b, a+b))
    elif n == 2:
        print('A multiplicação entre {} e {} é {}'.format(a, b, a*b))
    elif n == 3:
        if a - b > 0:
            print('Entre {} e {} o maior valor é {}'.format(a, b, a))
        if a - b < 0:
            print('Entre {} e {} o maior valor é {}'.format(a, b, b))
    elif n == 4:
        print('Informe os numeros novamente: ')
    elif n == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print(20*'=-')
time.sleep(2)
print('Fim do programa! Volte sempre')

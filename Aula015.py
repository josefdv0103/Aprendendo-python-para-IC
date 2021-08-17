#cont = 1
#while cont <= 10:
#    print(cont, '', end='')
#    cont += 1
#print('Acabou')

#cont = 1
#while True:
#    print(cont, '', end='')
#    cont += 1
#    if cont == 10000:
#        break
#print('Acabou')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos')


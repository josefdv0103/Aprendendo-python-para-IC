import random
print(20*'=-')
print('VAMOS JOGAR PAR OU ÍMPAR')
print(20*'=-')
cont = 0
while True:
    n = int(input('Diga um valor: '))
    e = str(input('Escolha par ou ímpar[P/I]: ')).upper().strip()
    c = random.randrange(0,11)
    s = n + c
    if s % 2 == 0:
        print(f'Você jogou {n} e o computador {c}. Total de {s} DEU PAR')
        if e == 'P':
            print('Você ganhou!')
        if e == 'I':
            print('Você perdeu!')
            break
    if s % 2 != 0:
        print(f'Você jogou {n} e o computador {c}.Total de {s} DEU IMPAR')
        if e =='I':
            print('Você ganhou!')
        if e =='P':
            print('Você perdeu!')
            break
    cont =+ 1
print(f'GAME OVER! Você venceu {cont} vezes')

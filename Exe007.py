#c = float(input('Qual o valor da sua casa? '))
#s = float(input('Qual o seu salario?'))
#q = int(input('Quanto anos você vai pagar?'))
#p = c/(q*12)
#if p <= s*0.3:
#   print('Você está elegivel para o emprestimo!')
#    print('E terá de pagar: R${:.2f}'.format(p))
#else:
#   print('Você está inelegivel para o empretimo!')

#s = int(input('Digite um número inteiro: '))
#print('''[ 1 ]Binário
#[ 2 ]Octa
#[ 3 ]Hexadecimal''')
#p = int(input('Escolha uma das bases para a conversão: '))
#if p == 1:
#    print('{} convertido para binário é igual a {}'.format(s, bin(s)[2:]))
#elif p == 2:
#    print('{} conertido para octal é igual a {}'.format(s, oct(s)[2:]))
#elif p == 3:
#    print('{} convertido em hexadecimal é igual a {}'.format(s, hex(s)[2:]))

#n1 = float(input('Digite o primeiro numero: '))
#n2 = float(input('Digite o segundo numero: '))
#if n1 > n2:
#    print('Primeiro numero é maior')
#elif n2 > n1:
#    print('O segundo numero é maior')
#elif n2 == n1:
#    print('Os dois valores sao iguais')

#a = int(input('Em que ano você nasceu? '))
#s = int(input('''Qual o seu sexo?
#Digite 1 para masculino e 2 para feminino: '''))
#if s == 1:
#    if 2021 - a  < 18:
#        print('''Quem nasceu em {} tem {} em 2021
#    Ainda faltam {} anos para o alistamento
#    Seu alistamento será em {}'''.format(a, 2021-a, a+18-2021, a+18))
#    elif 2021 - a  > 18:
#       print('''Quem nasceu em {} tem {} anos em 2021
#   Você já deveria ter se alistado a {} anos
#    Seu alistamento foi em {}'''.format(a, 2021-a, 2021-a-18, a+18))
#    else:
#        print('Você deve se alistar IMEDIATAMENTE')
#elif s == 2:
#    print('Você nao tem a obrigatoriedade de se alistar')

#n1 = float(input('Digite a sua primeira nota: '))
#n2 = float(input('Digite a sua segunda nota: '))
#if (n1+n2)/2 > 6.0:
#    print('O aluno teve media {.:2f} e está passado de ano'.format((n1+n2)/2))
#elif 3.5 < (n1+n2)/2 < 6.0:
#    print('O aluno teve media {:.2f} e esta em recuperação'.format((n1+n2)/2))
#else:
#   print('O aluno esta REPROVADO!')

#a = int(input('Digite o seu ano de nascimento: '))
#idade = 2021 - a
#if idade < 9:
#    print('''O atleta tem {}
#Classificação: {}'''.format(idade, 'mirim'))
#elif 9 <= idade < 14:
#   print('''O atleta tem {}'
#Classiicação: {}'''.format(idade, 'Infantil'))
#elif 14 <= idade < 19:
#   print('''O atleta tem {}
#Classificação: {}'''.format(idade, 'junior'))
#elif 19 <= idade < 25:
#   print('''O atleta tem {}
#Classificação: {}'''.format(idade, 'Senior'))
#elif idade > 20:
#   print('''O atleta tem {}
#Classificação: {}'''.format(idade, 'Master'))

#a = float(input('Primeiro segmento: '))
#b = float(input('Segundo segmento: '))
#c = float(input('Terceiro segmento: '))
#if a + b > c and a + c > b and b + c > a:
#   if a == b == c:
#       print('Pode formar um triangulo equlátero')
 #   elif a == b != c or a==c != b or b == c != a:
#       print('Pode formar um triangulo isosceles')
#    elif a != b != c:
#        print('Pode formar um triangulo escaleno')
#else:
#   print('Não forma triangulo esses segmentos')

#p = float(input('Qual o seu peso(Kg)?'))
#a = float(input('Qula o sua altura(m)?'))
#i = p/pow(a, 2)
#if i < 18.5:
#   print('''Seu IMC é igual a {}
#Sua classificação é de MAGREZA''')
#elif 24.9 > i > 18.5:
#   print('''Seu IMC é igual a {}
#Sua classificação é de NORMAL''')
#elif 25.0 < i < 29.9:
#   print('''Seu IMC é igual a {}
#Sua classificação é de SOBREPESO''')
#elif 30.0 < i <39.9:
#   print('''Seu IMC é igual a {}
#Sua classificação é de OBESIDADE''')
#else:
#   print('''Seu IMC é de {}
#Sua classificação é de OBESIDADE GRAVE''')

#print(20*'=','Loja do zé', 20*'=')
#print('{:=^40}'.format('Loja do zé'))
#p = float(input('Preço das compras:R$ '))
#print('''FORMAS DE PAGAMENTO
#[1] à vista dinheiro/cheque
#[2] à vista cartão
#[3] 2x no cartão
#[4] 3x ou mais no cartão''')
#o = int(input('Qual é a opção?'))
#if o == 1:
#    print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(p, p*0,9))
#elif o == 2:
#    print('Sua compra de R$ {:.2f} será o mesmo valor no final'.format(p))
#elif o == 3:
#    print('Sua compra de R$ {:.2f} irá custar R${:.2f} no final\nCom parcelas de R${:.2f}'.format(p, p+2*(p*0.05), p/2))
#elif o == 4:
#    v = int(input('Quantas parcelas?'))
#   print('Sua compra de R${} irá custar R${} no final\nCom parcelas de R${}'.format(p, p+p*0.05*v, (p+p*0.05)/v))
#else:
#    print('Opção inválida de pagamento. Tente novamente')

import random, time
j = ['PEDRA', 'PAPEL', 'TESOURA']
e = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada?: '''))
c = random.choice(j)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print(20*'=','''
Computador jogou {}
Jogador jogou {}\n{}'''.format(c, j[e], 20*'='))
if c == j[e]:
    print('EMPATE')
elif c == j[2] and j[e] == 'PAPEL' or c == j[0] and j[e] == 'TESOURA' or c == j[1] and j[e] == 'PEDRA':
    print('PERDEU')
else:
    print('VENCEU')

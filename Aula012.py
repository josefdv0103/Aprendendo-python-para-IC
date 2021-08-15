nome = str(input('Qual é o seu nome? '))
if nome == 'José':
    print('Que nome bonito')
elif nome == 'Maria' or nome == 'Jurema':
    print('Seu nome é igual a da minha vó')
elif nome in ('João Paulo'):
    print('É um nome que eu gosto')
else:
    print('Seu nome é bem normal')

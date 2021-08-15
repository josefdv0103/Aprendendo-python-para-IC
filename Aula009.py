print('''Não posso crer que se conceba
Do amor senão o gozo físico!
O meu amante morreu bêbado,
E meu marido morreu tísico!

Não sei entre que astutos dedos
Deixei a rosa da inocência.
Antes da minha pubescência
Sabia todos os segredos...''')#As aspas triplas ajudam a manter a formatação nesse caso de textos com quebra de linha

frase = "José Augusto Florentino Dela Vedova"
print(frase.upper().count('O'))#transformei em maiuscula e depois contei as maiusculas
print(len(frase))
print(frase.capitalize())
print(frase.split())
print('-'.join(frase.split()))
print(frase.replace('José', 'Luiz'))
print(frase.find('José'))
print('José'in frase)

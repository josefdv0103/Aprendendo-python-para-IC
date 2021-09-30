#TUPLAS
x = ('Hamburguer', 'Suco', 'Pizza')
#print(x[1])

#A MESMA COISA DE MANEIRAS DIFERENTES
#for comida in x:
#    print(f'Eu vou comer {comida}')
#for cont in range (0, len(x)):
#    print(f'Eu vou comer {x[cont]}')

#A MESMA COISA DE MANEIRAS DEIFERENTES
#for pos, comida in enumerate(x):
#    print(f'Eu vou comer {comida} na posição {pos}')
#for cont in range (0, len(x)):
#    print(f'Eu vou comer {x[cont]} na posição {cont}')

#ORDEM ALFABETICA
#print(sorted(x))

a = (2,5,4)
b = (5,8,1,2)

#A soma de tuplas colam uma na outra e a ordem da soma a + b e b + a interfere
#No resultado final
c = a + b
d = b + a
print(c)
print(d)
print(c.count(5))
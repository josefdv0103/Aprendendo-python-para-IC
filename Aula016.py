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

#a = (2,5,4)
#b = (5,8,1,2)

#A soma de tuplas colam uma na outra e a ordem da soma a + b e b + a interfere
#No resultado final
#c = a + b
#d = b + a
#print(c)
#print(d)
#print(c.count(5))#Quantas vezes o numero 5 aparece
#print(c.index(8))#Em que posição está o 8, 
#print(c.index(5, 2))#se tiver dois numeros iguais
#podemos usar uma virgula e especificar a partir de qual posição irermos
#querer ver o numero especificado

pessoa = ('Gustavo', 38, 'M', 67)#Numa tupla é possivel colocarmos elementos
#de diferentes tipos numeros, strings, ...
del(pessoa)#Para apagar uma tupla ou qualquer coisa em python
print(pessoa)

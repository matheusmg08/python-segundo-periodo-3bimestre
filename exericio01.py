"""
Escreva um programa que remova todos os elementos de uma lista que também estão presente em outra lista.
"""
lista1 = [4, 5, 2, 3, 1, 2, 5]
lista2 = [3, 1, 5, 8, 9]
lista1 = set(lista1)
lista2 = set(lista2) 
lista = lista1.difference(lista2)
print (lista)


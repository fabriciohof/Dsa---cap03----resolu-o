# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma lista

tupla = (4,2,5,1)
lista = []
for x in tupla:
    result  = x*2
    lista.append(result)
print(lista, type(lista))
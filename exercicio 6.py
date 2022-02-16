# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa


cont = 0 
while cont<100:
    if cont == 23:
        break
    print(cont)
    cont += 1
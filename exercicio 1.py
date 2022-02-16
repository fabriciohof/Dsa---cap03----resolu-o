# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

dias = input('Qual é o dia da semana?')

while dias == 'Sábado'or dias == 'Domingo':
    print('Hoje é dia de descanso')
    break
else:
    print('Você precisa trabalhar!')
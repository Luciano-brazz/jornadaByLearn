from random import randint
from time import sleep
v = 0
print('=' * 50)
print(f'{"BEM-VINDO ":^50}')
print(f'{" AO ":^50}')
print(f'{"PAR OU ÍMPAR ":^50}')
print('=' * 50)
print('Regras:')
print('''1 -> você deve escolher entre par ou impar
2 -> você deve esconher um nÚmero DO TIPO INTEIRO
3 -> O jogo só acaba quando você PERDE!!''')
print(f'{" BOA SORTE !!! ":^50}')
print('=' * 50)
while True:
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    jogador = int(input('digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else'DEU IMPAR')
    sleep(2)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('vamos jogar novamente...')
    print('-' * 50)
print('=' * 50)
print(f'{"GAME OVER!":^50}')
print('Calculando resultado... ', end='')
sleep(2)
print(f' Você VENCEU {v} vezes.')

# 5) Escreva um programa que inverta os caracteres de um string.

while True:
    n = input('Digite uma palavra: ')
    print(f'{n[::-1]}')
    
    co = ' '
    
    while co not in 'SN':
        co = input('Deseja continuar? [ S / N ]: ').upper()
    if co == 'N':
        break
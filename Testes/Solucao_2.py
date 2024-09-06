#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
 
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

p =  r = 0
s = 1
n = int(input('Digite um numero: '))

while p < n:
    
    r = p + s
    p = s
    s = r
      
    print(p, end='')
    print(' → ', end='')
    
if n == p:
    print(f'O numero {n} pertence a sequência de Fibonacci')
else:
    print(f'O numero {n} não pertence a sequência de Fibonacci')
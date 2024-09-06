# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


#Lista
valores = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]

#Contadores
co = com = 0

#loop que percorre o tamanho da lista e especifica os valores e os dias de faturamento
for d in range(len(valores) + 1 - 1):
    print('==' * 20)
    print(f'{d + 1}° Dia\nValor: {valores[d]:.2f}')

#Nesse loop estou acrescentando um valor ao contador co para todo o numero que não for zero
for z in valores:
    if z != 0:
        co += 1
 

# Aqui eu estou percorrendo os indices da lista e acrescentando +1 para poder passar o numero correto do dia e o maior valor da lista     
for i, v in enumerate(valores):
    if v == max(valores):
        print('==' * 20)          
        print(f'O maior valor de faturamento foi o de {max(valores):.2f}, ocorrido no {i + 1}° dia do mês')
  
# Esse loop era para descobrir o menor valor porém foi necessaria a verificação fora do loop para não contabilizar os zeros como os menores indices.
mi = min([v for v in valores if v != 0])
for i, v in enumerate(valores):
    if v == mi:
        print('==' * 20)
        print(f'O menor valor de faturamento foi o de {mi:.2f}, ocorrido no {i + 1}° dia do mês')

# Com a função sum estou somando os valores da lista
so = sum(valores)
# Aqui é o valor da média com os valores somados e divindo pelo valor do contador co
me = so / co

# Loop para verificar os numeros maiores que o valor da média e um contador para dizer quantos são
for u in valores:
    if u > me:
        com += 1
print('==' * 20)
print(f'Em {com} dias esse mês o valor do faturamento diario ultrapassou a média mensal de: {me:.2f}')
        






    

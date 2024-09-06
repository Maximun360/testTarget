# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
ou = 19849.53

l = [sp, rj, mg, es, ou]
n = ['SP','RJ', 'MG', 'ES', 'OU']
s = sum(l)

for p, uf in zip(l, n):   
    c = p / s * 100
    print(f'{uf}: R$ {p} = {c:.2f}%')
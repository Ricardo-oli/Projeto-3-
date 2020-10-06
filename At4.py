pessoas = 0
alt_inf = 0
alt_ent = 0
alt_sup = 0

for pessoas in range(10):
    altura = float(input('Altura: '))
    if altura < 1.6:
        alt_inf += 1
    elif 1.8 >= altura >= 1.6:
        alt_ent += 1
    else:
        alt_sup += 1

print(f'Total de pessoas cadastradas {pessoas+1}.')
print(f'Pessoas com altura inferior a que 1,60 metros: {alt_inf}')
print(f'Pessoas com altura entre 1,60 e 1,80: {alt_ent}')
print(f'Pessoas com altura superior a 1,80 metros: {alt_sup}')
print(input('Nome do time: '))
v = int(input('Vitórias: '))
d = int(input('Derrotas: '))
e = int(input('Empates: '))
total = v + d + e
p = v * 3 + e
vitorias = v * 3
pontos_perdidos = d * 3
print('Total de Partidas:', int(total),'Partidas')
print('Total de Pontos:', p,'Pontos')
print('Total de pontos perdidos:', pontos_perdidos)
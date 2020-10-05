Aluno = input ('Insira o seu nome:')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segundaa nota: '))
média = (nota1 + nota2) / 2
print('Notas {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 7:
    print('Sob Recuperção.')
elif média < 7:
    print('REPROVADO.')
else:
    print('APROVADO.')
nomeAluno = input('Digite seu primeiro nome: ')
nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))
nota3 = float(input('Digite a 3° nota: '))
nota4 = float(input('Digite a 4° nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print('\nCauculo:')
print('({} + {} + {} + {}) / 4' .format(nota1, nota2, nota3, nota4))
print('{} / 4' .format(nota1 + nota2 + nota3 + nota4))
print('{}' .format(media))

if (media >= 6):
    print('-' *30)
    print('|Aluno: {}\n|Media Final: {}\n|Foi aprovado!' .format(nomeAluno, media))
    print('-' * 30)
else:
    print('-' * 30)
    print('|Aluno: {}\n|Media Final: {}\n|Foi reprovado!' .format(nomeAluno, media))

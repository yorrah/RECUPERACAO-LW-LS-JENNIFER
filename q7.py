macho = 0
femea = 0

for i in range(0, 5):
    nome = input('escreva seu nome: ')
    sexo = str(input('escreva seu sexo: '))
    
    if sexo == 'masculino':
        macho = macho + 1
        print('você é homem')
    elif sexo == 'feminino':
        femea = femea + 1
        print('você é mulher')

print('o numero de mulheres é : {}' .format (femea))
print('o numero de mulheres é : {}' .format (macho))


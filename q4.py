nome = input("Informe o nome do aluno: ")
nota1= float(input("Uma nota? "))
nota2= float(input("Uma segunda nota? "))
nota3= float(input("Uma terceria nota? "))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print('O aluno {} está aprovado. Sua média é:{:.2f}' .format(nome,media))

elif media <= 5:
    print('O aluno', nome, 'está reprovado. Sua média é: ', media)

elif (media >= 5.1) and (media <= 6.9):
    print('O aluno', nome, 'está em recuperação. Sua média é: ', media)







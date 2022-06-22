preco = 0
precocusto = 0

for i in range (0, 40):
    p = int(input('preço do produto: '))
    pc= int(input('preço de custo de produto: '))

    preco = preco + p
    precocusto = precocusto + pc

    if preco > precocusto:
        print ('Lucro.')

    else:
        print('Não obtece lucro.')

print('a média dos preços é: %d' %(preco+precocusto)/2)
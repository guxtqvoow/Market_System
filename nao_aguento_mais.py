RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

pagamento = 0

print('Qual alimento voce deseja adquirir na loja? (X) para finalizar pedido e  \nR$10 Arroz \nR$5 Feijao \nR$3 Óleo\n ')

while True:
    x = input('').lower()

    if x == 'arroz':
        pagamento += 10
        print(f'O alimento que você {GREEN}comprou{RESET} custa {GREEN}R$10,00{RESET} e a soma total da sua compra é de {GREEN}R${pagamento}{RESET}')

    elif x == 'feijao' or x == 'feijão':
        pagamento += 5
        print(f'O alimento que você {GREEN}comprou{RESET} custa {GREEN}R$5,00{RESET} e a soma total da sua compra é de {GREEN}R${pagamento}{RESET}')

    elif x == 'óleo' or x == 'oleo':
        pagamento += 3
        print(f'O alimento que você {GREEN}comprou{RESET} custa {GREEN}R$3,00{RESET} e a soma total da sua compra é de {GREEN}R${pagamento}{RESET}')

    elif x == '-arroz':
        pagamento -= 10
        print(f'O alimento que você {RED}tirou{RESET} custa {RED}R$10,00{RESET} e a soma total da sua compra é de {RED}R${pagamento}{RESET}')

    elif x == '-feijao' or x == '-feijão':
        pagamento -= 5
        print(f'O alimento que você {RED}tirou{RESET} custa {RED}R$5,00{RESET} e a soma total da sua compra é de {RED}R${pagamento}{RESET}')

    elif x == '-oleo' or x == '-óleo':
        pagamento -= 3
        print(f'O alimento que você {RED}tirou{RESET} custa {RED}R$3,00{RESET} e a soma total da sua compra é de {RED}R${pagamento}{RESET}')

    elif x == 'x' and pagamento < 0:
        print(f'Você não pode finalizar um pedido com valor negativo, o valor da sua compra foi estornada à ZERO.')
        pagamento = 0

    elif x == 'x' and pagamento >= 0:
        print(f'O resultado da compra foi de R${pagamento}')
        break

    else:
        print('Erro desconhecido, tente novamente')

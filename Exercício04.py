#Nicolas Lamback de Paulo
opcao = 0
saldo = float(0)
saque = 0, 0
deposito = 0, 0
while opcao != 4:
    opcao = int(input('''
===Banco===
[ 1 ] Consultar saldo
[ 2 ] Saque
[ 3 ] Depósito
[ 4 ] Sair
Qual operação deseja realizar:\n '''))
    if opcao == 1:
        print('O seu saudo é de: ', saldo)
    elif opcao == 2:
        saque = float(input('Digite quanto deseja sacar: '))
        if saldo - saque < 0:
            print('Saldo indisponível, trabalhe mais!')
        else:
            print(f'Saque de {saque} reais realizado com sucesso!')
            saldo = saldo - saque
    elif opcao == 3:
        deposito = float(input('Digite quanto deseja depositar: '))
        print(f'{deposito} reais depositados!')
        saldo = saldo + deposito
    elif opcao == 4:
        print('Obrigado pela preferência!')
    else:
        print('Opção inválida! Tente novamente.')

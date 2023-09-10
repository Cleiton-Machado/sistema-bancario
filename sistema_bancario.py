menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
cheque_especial = 500
extrato = ''
numero_saque = 0
limite_saque = 500
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input('Valor do depósito: '))
        if valor <= 0:
            print('Operação falou, o valor informado é inválido')
            continue
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
    elif opcao == 's':
        if numero_saque < LIMITE_SAQUES:
            valor = float(input('Informe o valor do saque: '))
            if valor <= saldo + cheque_especial:
                if valor <= 0:
                    print('Operação falou, o valor informado é inválido')
                    continue
                if valor > limite_saque:
                    print('Operação falou, o valor informado é inválido')
                    continue
                saldo -= valor
                extrato += f'Saque: R$ {valor:.2f}\n'
                numero_saque += 1
            else:
                print('Saldo insuficiente')
        else:
            print('Limite de saques atingido')
    elif opcao == 'e':
        print('Extrato'.center(40, '='))
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print('-' * 40)
        if saldo < 0:
                print(f'Saldo: R$ {saldo:.2f}\nLimite cheque especial: R$ {cheque_especial:.2f}\n Saldo + Cheque Especial: R${saldo + cheque_especial:.2f}')
        else:
            print(f'Saldo: R$ {saldo:.2f}\nLimite cheque especial: R$ {cheque_especial:.2f}\nSaldo + Cheque Especial: R${saldo + cheque_especial:.2f}')
        print('-' * 40)

        
    elif opcao == 'q':
        break
    else:
        print('Opção inválida, por favor selecione uma opção válida.')
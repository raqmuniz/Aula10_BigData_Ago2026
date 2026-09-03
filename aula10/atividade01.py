try: #tente executar
    saldo = 1000
    saque = float(input('Quanto deseja sacar? '))

except Exception as e: #se der esse erro execute a linha abaixo
    print('Informe o valor corretamente: {e}')

else: #se não der erro passa para a próxima etapa
    if saque > saldo:
        print('Saldo insuficiente')

    elif saque < 2:
        print(f'\nO valor do saque deve ser a partir de R$ 2,00')

    else:
        #saldo = saldo - saque essa expressão se escreve conforme abaixo
        saldo -= saque
        print('\nSaque realizado')
        print(f'Saldo restante R$ {saldo:.2f}')

finally:
    print('Operação finalizada')

print('\nSessão encerrada!')

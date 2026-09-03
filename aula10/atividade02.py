try:
    total_peixes = 100
    calculo_excesso = int(input('Quantos quilos foram pescados: '))

except ValueError:
    print('Informe o valor corretamente')

else:
    if calculo_excesso <= 0:
        print('O valor digitado deve ser maior que zero')

    else: 
        print('\nValor registrado')
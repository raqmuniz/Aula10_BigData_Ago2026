try:
    total_vendido = float(input('Total R$: '))
    qtd = int(input('Quantidade vendida: '))
    media_vendedor = total_vendido / qtd
    

except (ValueError, TypeError):
    print(f'Erro: Informe apenas os números')

except KeyboardInterrupt:
    print('Programa finalizado pelo usuário')

except ZeroDivisionError:
    print(f'\nErro - A quantidade não pode ser zero')

else: #se não der erro
    print(f'Média das vendas: R$ {media_vendedor}')

finally: 
    print('Operação finalizada!')
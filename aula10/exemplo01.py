# Exemplos
# preco = float(input('Preço: '))
# quantidade = int(input('Quantidade: '))
# total = preco * quantidade

# print(f'Total: {total}')

#Exemplo 01
# try: #tente executar
#     preco = float(input('Preço: '))
#     quantidade = int(input('Quantidade: '))
#     total = preco * quantidade

#     print(f'Total: {total}')

# except ValueError: # Se der erro, execute aqui
#     print(f'\nErro: Inorme apenas número: ')




#Exemplo 02
# try: 
#     total_vendido = float(input('Total R$: '))
#     qtd = int(input('Quantidade vendida: '))
#     media_vendedor = total_vendido / qtd
#     print(f'Média das vendas: {media_vendedor}')


# except (ValueError, TypeError):
#     print(f'\nErro: Inorme apenas número ')
# except ZeroDivisionError:

#     print(f'\nErro - a quantidade não pode ser zero ')


#Exemplo03
#Média para 5 vendedores
# for i in range(5):
#     total_vendido = float(input('Total R$: '))
#     qtd = int(input('Quantidade vendida: '))
#     media_vendedor = total_vendido / qtd
#     print(f'Média das vendas: {media_vendedor}')

for i in range(5):
    try: 
        total_vendido = float(input('Total R$: '))
        qtd = int(input('Quantidade vendida: '))
        media_vendedor = total_vendido / qtd
        print(f'Média das vendas: {media_vendedor}')

    except (ValueError, TypeError):
        print(f'\nErro: Inorme apenas número ')

    except KeyboardInterrupt:
        print('Programa finalizado pelo usuário')
        exit()

    except ZeroDivisionError:

     print(f'\nErro - a quantidade não pode ser zero ')
     
from banco import obterConta, banco

def sacar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] -= valor
            print('tirei dinheiro dele mami')
        else:
            print('macho cria vergonha tu é um liso')
    else:
        print('existe não fi')


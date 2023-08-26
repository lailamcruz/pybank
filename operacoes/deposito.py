from banco import obterConta,banco

def depositar(conta: int, valor:float) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] += valor
    else:
        print('essa praga nem existe mo')



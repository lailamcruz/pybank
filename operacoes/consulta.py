from banco import obterConta, banco


def consultarSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f"Seu saldo: {cliente['saldo']}")
    else:
        print("essa praga nem existe ma deixa de mentir")

consultarSaldo(1)
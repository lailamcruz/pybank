from banco import obterConta, banco

def transferir(origem: int, destino: int, valor: float) -> None:
    contaOrigem = obterConta(origem)
    contaDestino = obterConta(destino)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -= valor
            contaDestino['saldo'] += valor
            print('todo dia um malandro e um otário saem de casa')
        else:
            print('sai daí liso')


    else:
        print('uma ou mais contas são lavagem de dinheiro')
print(banco)
transferir(2,1,5)
print(banco'')
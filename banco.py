# quando o retorno de uma função é opcional diz assim

from typing import Optional



banco = [
    {"conta": 1, "cliente": "laila", "saldo": 4.50},
    {"conta": 2, "cliente": "jão", "saldo": 9.00},
]

conta_atual = 2

def adicionarConta(nome: str, saldo: float) -> None:
    global conta_atual
    conta_atual += 1
    conta = {
        "conta": conta_atual,
        "cliente": nome,
        "saldo": saldo
    }
    banco.append(conta)
    print("conta cadastrada viado!!!")

# adicionarConta("anitta", 1054010654)
# print(banco)
#
# adicionarConta("miley", 105)
# print(banco)

def obterConta(conta:int) -> Optional[dict or None]:
    for cliente in banco:
        if cliente['conta'] == conta:
            return cliente
    return None

# print(obterConta(3))
#
# print(obterConta(10))

def buscarCliente(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f"N. conta: {cliente['conta']}")
        print(f"Nome: {cliente['cliente']}")
        print(f"Saldo: {cliente['saldo']}")
    else:
        print("cliente doesnt exist bitch")

# buscarCliente(1)
# buscarCliente(10)

def listarTodos() -> None:
    for cliente in banco:
        buscarCliente(cliente['conta'])
        print('------------------------')

# listarTodos()

def editarNome(conta: int, novo_nome: str) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['cliente'] = novo_nome
        print('dados alterados mo')
    else:
        print('encontrei esse doido não bb')


def removerConta(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        banco.remove(cliente)
        print('removi essa praga')
    else:
        print("essa praga nem existe")
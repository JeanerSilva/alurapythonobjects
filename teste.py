from Conta import Conta


def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))


conta1 = Conta(123, "Jeaner", 100, 1000)
conta1.saca(20)
print (conta1.saldo)

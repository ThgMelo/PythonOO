from conta import Conta

conta = Conta(123, "Thiago", 55.0, 1000.0)
print("\n")
conta2 = Conta(321, "Marco", 100.0, 1000.0)

valor = 10.0

conta2.saca(valor)
conta.deposita(valor)

print("\n")

conta.extrato()
conta2.extrato()

conta.transfere(10, conta2)
conta.extrato()
conta2.extrato()

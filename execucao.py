from conta import Conta

conta = Conta(123, "Thiago", 55.0, 1000.0)
print("\n")
conta.extrato()
conta.deposita(100)
conta.extrato()
conta.saca(50)
conta.extrato()
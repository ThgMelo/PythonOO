from conta import Conta

conta = Conta(123, "Thiago", 55.0, 1000.0)
print("\n")

print(conta.get_limite())
print(conta.get_saldo())
print(conta.get_titular())

conta.set_limite(10000)
print(conta.get_limite())
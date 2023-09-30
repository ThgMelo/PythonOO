from conta import Conta

conta = Conta(123, "Thiago", 55.0, 1000.0)
print(f"Número: {conta.numero}")
print(f"Titular: {conta.titular}")
print(f"Saldo: {conta.saldo}")
print(f"Limite: {conta.limite}")
print("\n")


conta2 = Conta(123, "Marco", 100.0, 1000.0)
print(f"Número: {conta2.numero}")
print(f"Titular: {conta2.titular}")
print(f"Saldo: {conta2.saldo}")
print(f"Limite: {conta2.limite}")
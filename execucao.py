from conta import Conta
from cliente import Cliente

conta = Conta(123, "Thiago", 55.0, 1000.0)
conta.limite = 20000
print(conta.limite)
print("\n")

cliente = Cliente("thiago")
print(cliente.nome)

cliente.nome = "duda"
print(cliente.nome)
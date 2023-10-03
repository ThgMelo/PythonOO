from conta import Conta
from cliente import Cliente

conta = Conta(123, "Thiago", 55.0, 1000.0)
print(Conta.codigo_banco())
codigos = Conta.codigos_bancos()
print(codigos['Caixa'])
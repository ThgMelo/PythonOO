from conta import Conta

conta = Conta(123, "Thiago", 55.0, 1000.0)
print("\n")
#print(conta.__limite) aqui lança erro
print(conta._Conta__limite) # podemos acessar indiretamente
class Conta:

    def __init__(self, numero, titular, saldo, limite): # Função construtora // self é a referência que sabe encontrar objeto criado
        print(f"Construindo objeto... {self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo de {self.saldo} do titular {self.titular}")

    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        self.saldo -= valor
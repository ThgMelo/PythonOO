class Conta:

    def __init__(self, numero, titular, saldo, limite): # Função construtora // self é a referência que sabe encontrar objeto criado
        print(f"Construindo objeto... {self}")
        self.__numero = numero # __ = atributo privado
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
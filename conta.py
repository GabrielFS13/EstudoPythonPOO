

class Conta:
    #características = atributos

    # def __init__(self): função construtura
    def __init__(self, numero, titular, saldo, limite):
        #self serve para acessar o objeto e defenir os att
        print("Objeto Contruido")
        # __ <- private
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

        
    #métodos
    def extrato(self):
        print(f"Saldo {self.__saldo} do titutar {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.sal__saldodo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #Getters, nunca altera
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def get_limite(self):
        return self.__limite
        
    #Setters, altera valores, somente isso.
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
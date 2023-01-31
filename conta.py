

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

    #método privado
    def __pode_sacar(self, valor_a_sacar):
        disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Valor acima do limite!")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #Getters, nunca altera
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular

    @property
    def get_limite(self):
        return self.__limite
        
    #Setters, altera valores, somente isso.
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {
            'BB': "001",
            'Caixa': "104",
            'Bradesco': "237"
        }
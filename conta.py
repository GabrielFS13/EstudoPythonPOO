

class Conta:
    #características = atributos

    # def __init__(self): função construtura
    def __init__(self, numero, titular, saldo, limite):
        #self serve para acessar o objeto e defenir os att
        print("Objeto Contruido")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

        
    #métodos
    def extrato(self):
        print(f"Saldo {self.saldo} do titutar {self.titular}")

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
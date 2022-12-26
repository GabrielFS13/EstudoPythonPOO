

class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    #propriedade -- mesmo nome da variavel, DEVE SER PRIVADO
    @property
    def nome(self):
        return self.nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
class Programa:

    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.__likes}"
    

class Filme(Programa):
    #chama a classe mãe
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    #representação textual do objeto
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} - {self.likes}'



class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    #representação textual do objeto
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} - {self.likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    #fala q é inteiravel (agora ele pode passar por um FOR pra pegar todos os itens vindos de uma lista)
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagram(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

play = [vingadores, atlanta]

for programa in play:
    print(programa)
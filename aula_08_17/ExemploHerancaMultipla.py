from Classes import Animal

class Voar(Animal):

    def voar(self):
        pass

class Nadar(Animal):

    def nadar(self):
        pass

class Pato(Voar, Nadar):

    def voar(self):
        print(f"O Pato {self.nome} está voando")

    def nadar(self):
        print(f"O Pato {self.nome} está nadando")

    def emitir_som(self):
        print(f"O Pato {self.nome} fazendo gua gua gua")

class Peixe(Nadar):

    def nadar(self):
        print(f"O Peixe {self.nome} está nadando")

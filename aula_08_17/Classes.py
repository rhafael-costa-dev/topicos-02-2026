class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def _apresentar(self):
        print(f'Olá meu nome é {self.nome},  tenho {self.idade} anos')


class Animal:

    def __init__(self, nome):
        self.nome = nome
        self.esta_vivo = True

    def emitir_som(self):
        print("Som bla bla bla bla")

    def apresentar(self):
        pass


class Gato(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome)
        self.idade = idade

    def emitir_som(self):
        print("Miau")

    def apresentar(self):
        print(f"Gato -> {self.nome}, {self.esta_vivo}, {self.idade}")


class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au Au")



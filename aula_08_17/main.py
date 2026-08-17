from Classes import Pessoa, Gato, Cachorro
from ExemploHerancaMultipla import Pato, Peixe

print("### Exemplo de Classes")
pessoa1 = Pessoa("Jose", 20)
pessoa1._apresentar()

pessoa2 = Pessoa('Ana', 25)
pessoa2._apresentar()

print("########################")
print("### Exemplo de Herança")
gato = Gato('Bichano', 10)
gato.apresentar()
gato.emitir_som()

c = Cachorro("Scoob")
c.apresentar()
c.emitir_som()

print("########################")
print("### Exemplo de Herança Múltipla")

peixe = Peixe('Peixinho')
peixe.nadar()

pato = Pato("Patolino")
pato.voar()
pato.nadar()
pato.emitir_som()

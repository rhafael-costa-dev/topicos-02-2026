resto = int(input("Informe o valor: "))
resposta = { }
notas = [200, 100, 50, 20, 10, 5, 2]


for nota in notas:
    qtd_notas = resto // nota
    if qtd_notas > 0:
        resto = resto % nota
        resposta[nota] = qtd_notas

for chave, valor in resposta.items():
    print(f"{valor} notas de R$ {float(chave)}")


for e in resposta.keys():
    print(e)

for i in resposta.values():
    print(i)



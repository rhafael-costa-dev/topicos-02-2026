resto = int(input("Informe o valor: "))
notas = [200, 100, 50, 20, 10, 5, 2]

for nota in notas:
    qtd_notas = resto // nota
    if qtd_notas > 0:
        resto = resto % nota
        print(f"{qtd_notas} notas de R$ {float(nota)}")


print(f"Resto {resto}")




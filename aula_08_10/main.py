resto = int(input("Informe o valor: "))

nota = 200

while nota > 0:

    qtd_notas = resto // nota
    if qtd_notas > 0:
        resto = resto % nota
        print(f"{qtd_notas} notas de R$ {float(nota)}")

    match(nota):
        case 200: nota = 100
        case 100: nota = 50
        case 50: nota = 20
        case 20: nota = 10
        case 10: nota = 5
        case 5: nota = 2
        case 2: nota = 0

print(f"Resto {resto}")



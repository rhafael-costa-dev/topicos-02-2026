import csv

f = [[10, 'José da Silva', 'Advogado', 1000.00]]
with open('dados/dados_csv.csv', 'a', newline='', encoding='utf-8') as arq:
    escritor = csv.writer(arq, delimiter=',')
    escritor.writerows(f)
c = ['id', 'nome', 'cargo', 'salario']
d = [{'id': 11, 'nome': 'João', 'cargo': 'Analista', 'salario': 5000.00}]
with open('dados/dados_csv.csv', 'a', newline='', encoding='utf-8') as arq:
    escritor = csv.DictWriter(arq, fieldnames=c)
    escritor.writerows(d)

"""
with open('dados/dados_csv.csv', 'r', encoding='utf-8') as arq:
    leitor = csv.reader(arq,  delimiter=',')
    cabecalho = next(leitor)
    print(cabecalho)
    for linha in leitor:
        nome, cargo, salario = linha[1], linha[2], float(linha[4])
        print(f'{nome} atua como {cargo} e tem o salatio {salario}')
"""

print()
print()
with open('dados/dados_csv.csv', 'r', encoding='utf-8') as arq:
    leitor_dict = csv.DictReader(arq, delimiter=',')
    for registro in leitor_dict:
        print(f"Func: {registro['nome']} - Cargo: {registro['cargo']}")





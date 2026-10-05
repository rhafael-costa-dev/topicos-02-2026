from pathlib import Path

a = Path('dados/dados_txt2.txt')
if a.exists():
   print('Existe')
else:
    print('Não existe')

exit()

arquivo = open('dados/dados_txt.txt', 'a', encoding='utf-8')
arquivo.write('Novo conteúdo\n')
arquivo.close()

arquivo = open('dados/dados_txt.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

arquivo = open('dados/dados_txt.txt', 'r', encoding='utf-8')
for linha in arquivo:
    print(linha.strip())
arquivo.close()

print()
with open('dados/dados_txt.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

print(f'Total de linhas ${len(linhas)}')

try:
    with open('dados_inexistentes.txt', 'r', encoding='utf-8') as arq:
        conteudo = arq.read()
except FileNotFoundError:
    print("Erro: O arquivo solicitado não foi encontrado no diretório.")
except PermissionError:
    print("Erro: Você não tem permissão para ler este arquivo.")
except Exception as e:
    print(f"Erro inesperado: {e}")

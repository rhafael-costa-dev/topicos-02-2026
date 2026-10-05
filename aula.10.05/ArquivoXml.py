import xml.etree.ElementTree as ET
tree = ET.parse('dados/dados_xml.xml')
root = tree.getroot()
print(f"Tag Raiz: {root.tag}")
# Iterar sobre os elementos filhos
for elem in root.findall('departamento'):
    for f in elem.findall('funcionario'):
        # Acesso a atributos da tag
        print(f.get('nome'))

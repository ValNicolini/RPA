import xml.etree.ElementTree as ET

def capturar_nprocesso(xml_path):
    # Análise do arquivo XML
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Lista para armazenar os resultados
    resultados = []

    # Iteração através dos elementos do XML
    for elemento in root.iter():
        # Verifica se o elemento é do tipo 'NPROCESSO'
        if elemento.tag == 'NPROCESSO':
            resultados.append(elemento.text)

    return resultados

# Exemplo de uso
caminho_do_xml = r'C:\xampp\htdocs\GitHub\Extrator_url\ADVOCACIAHCOSTA - (120)_8_.xml'
resultados = capturar_nprocesso(caminho_do_xml)

# Imprime os resultados capturados
for resultado in resultados:
    print(resultado)
print(len(resultados))

# pip isntall xmltodict
# pip install pandas
# pip install openpyxl

import xml.etree.ElementTree as ET
from tabulate import tabulate
import pandas as pd
import xmltodict

caminho_pasta = 'C:/NotasXML/'
arquivo_nota = '23240106147451001961550010002889461718548795.xml'
caminho_NFE = caminho_pasta + arquivo_nota

# Lendo o arquivo xml
with open(caminho_NFE, "r") as arquivo:
    conteudo = arquivo.read()

# Analise o XML para um dicionário
dados = xmltodict.parse(conteudo)

# Extrair os dados relevantes do XML
cabecalho = dados['nfeProc']['NFe']['infNFe']
numero = cabecalho['ide']['nNF']
data_emissao = cabecalho['ide']['dhEmi']
emitente = cabecalho['emit']['xNome']
destinatario = cabecalho['dest']['xNome']
itens = cabecalho['det']

# Criar uma lsta de dicionários com os dados dos itens
lista_itens = []
totalNF = 0

for item in itens:
    totalNF += float(item['prod']['vProd'])

for item in itens:
    lista_itens.append({
        'Numero da Nota': numero,
        'Data de emissao': data_emissao,
        'Total da NF': totalNF,
        'Emitente': emitente,
        'Destinatario': destinatario,
        'Item': item['@nItem'],
        'Codigo': item['prod']['cProd'],
        'Descricao': item['prod']['xProd'],
        'Quantidade': float(item['prod']['qCom']),
        'Preco Unitario': float(item['prod']['vUnCom']),
        'Total Item': float(item['prod']['vProd'])
    })

# Criando um dataframe do pandas
df = pd.DataFrame(lista_itens)

#Salvar conteúdo no excel
caminho_excel = caminho_pasta + numero + '.xlsx'
df.to_excel(caminho_excel, index=False)
print(f'Arquivo salvo na pasta! {caminho_excel}')


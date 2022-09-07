## Bibliotecas 
from subprocess import Popen
import os

""" Devido a que o arquivo de origem está em um formato antigo do excel (xls) e por
conter uma tabela dinamica a onde os dados estão ocultos no cache ("Pivot Cache")
se faz necessária a conversão do arquivo via libre office para poder acessar 
aos dados internos da planilha. """

def converter_excel():
    print("Iniciando conversão da planilha..")
    dados = Popen(['libreoffice', '--headless', '--convert-to', 'xls', '--outdir',
               'dados/dados_finais', './dados/dados_raw/vendas-combustiveis-m3.xls'])
    dados.communicate()
    print("Planilha convertida!")
    print("Apagando o arquivo original...")
    os.remove("./dados/dados_raw/vendas-combustiveis-m3.xls")
    print("Arquivo Excluído!")
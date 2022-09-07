## Bibliotecas

import pandas as pd
import os
import shutil

## Função para extrair dados do excel e criar um csv final para consumo


def extrair_dados(tabela,sheet):
    # Lendo o excel
    excel = pd.read_excel('./dados/dados_finais/vendas-combustiveis-m3.xls', sheet_name=sheet)
    # Selecionando as colunas
    if (sheet == 1):
        print("Lendo Sheet Vendas Derivados...")
        excel.columns = ['Product', 'Created_at', 'Região', 'UF','Unit', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'Total']
    else:
        print("Lendo Sheet Diesel...")
        excel.columns = ['Product', 'Created_at', 'Região', 'UF','Unit', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    #excel.columns = ['Product', 'Created_at', 'Região', 'UF','Unit', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'Total']
    # Remodelando o dataframe usando o "melt" e jogando os dados não mapeados na coluna value e na coluna variable
    excel = excel.melt(id_vars=['Product', 'Created_at', 'Região', 'UF','Unit'])
    ## Excluindo as linhas com nome "Total" da coluna variable para manter apenas os dados de data
    excel = excel.loc[excel['variable'] != 'Total']
    ## Criando a coluna year_month usando a coluna created_at e o dados da coluna variable
    excel['year_month'] = excel['Created_at'].astype(str) + '-' + excel['variable']
    ## Convertendo a coluna year_month para data
    excel['year_month'] = pd.to_datetime(excel['year_month'])
    ## Excluíndo colunas não utilizadas
    excel = excel.drop(labels=['variable', 'Região'], axis=1)
    ## Renomeando coluna value
    excel = excel.rename(columns={'value':'volume'})
    ## Fazendo tratamento das colunas e retirando os valores 'Nan'
    excel = excel.fillna(0)
    excel['volume'] = pd.to_numeric(excel['volume'])
    ## Criando arquivo csv para processamento
    excel.to_csv("dados/dados_finais/" + tabela + ".csv",index=False)
    ## Enviando o arquivo para o diretorio /tmp/airbyte_local/
    if os.path.exists("/tmp/airbyte_local/" + tabela + ".csv"):
        print("Removendo o arquivo..")
        os.remove("/tmp/airbyte_local/" + tabela + ".csv")
        print("Enviando o arquivo para /tmp/airbyte_local/ para o processamento pelo airbyte")
        shutil.copy('dados/dados_finais/' + tabela + '.csv', "/tmp/airbyte_local/")
    else:
        print("Não é necessário remover o arquivo..")
        print("Enviando o arquivo para /tmp/airbyte_local/ para o processamento pelo airbyte")
        shutil.copy('dados/dados_finais/' + tabela + '.csv', "/tmp/airbyte_local/")


    
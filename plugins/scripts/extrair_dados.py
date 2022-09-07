## Bibliotecas

import pandas as pd
import os

## Função para extrair dados do excel e criar um csv final para consumo


def extrair_dados(tabela,sheet):
    # Lendo o excel
    excel = pd.read_excel('./dados/vendas-combustiveis-m3.xls', sheet_name=sheet)
    # Selecionando as colunas
    excel.columns = ['Product', 'Created_at', 'Região', 'UF','Unit', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'Total']
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
    excel.to_csv('dados/' + tabela + '.csv')
    ## Apagando arquivo original
    os.remove("./dados/vendas-combustiveis-m3.xls")   


    

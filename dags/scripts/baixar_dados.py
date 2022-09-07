## Bicliotecas 
from urllib import request

## Baixar os dados do site GOV - ANP - DADOS ESTATÍSTICOS 

def baixar_dados():
    print("Baixando Arquivo")
    file_url = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/vdpb/vendas-combustiveis-m3.xls'
    destino = './dados/dados_raw/vendas-combustiveis-m3.xls'
    request.urlretrieve(file_url,destino)
    print("Arquivo baixado!")



## Bicliotecas 

from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator

from scripts.baixar_dados import baixar_dados
from scripts.converter_excel import converter_excel
from scripts.extrair_dados import extrair_dados
from scripts.conectar_postgree import conectar_postgree


with DAG('raizen_etl', 
        description='Job para extrair dados relacionados a venda de combustíveis do governo. ',
        start_date=datetime.today(), 
        catchup=False) as dag:

        baixar_xls = PythonOperator(
        task_id='baixar_xls', 
        python_callable=baixar_dados,
        dag=dag)

        converter_xls  = PythonOperator(
        task_id='converter_xls', 
        python_callable=converter_excel,
        dag=dag)

        extrair_xls_01  = PythonOperator(
        task_id='extrair_xls_venda_derivados', 
        python_callable=extrair_dados,
        op_kwargs={'tabela': 'venda_derivados', 'sheet': 1},
        dag=dag)

        extrair_xls_02  = PythonOperator(
        task_id='extrair_xls_venda_diesel', 
        python_callable=extrair_dados,
        op_kwargs={'tabela': 'venda_diesel', 'sheet': 3},
        dag=dag)

        inserir_dados_derivados  = PythonOperator(
        task_id='inserir_dados_derivados', 
        python_callable=conectar_postgree,
        op_kwargs={'tabela': 'venda_derivados'},
        dag=dag)

        inserir_dados_diesel  = PythonOperator(
        task_id='inserir_dados_diesel', 
        python_callable=conectar_postgree,
        op_kwargs={'tabela': 'venda_diesel'},
        dag=dag)

baixar_xls >> converter_xls >> [extrair_xls_01, extrair_xls_02] >> inserir_dados_derivados >> inserir_dados_diesel


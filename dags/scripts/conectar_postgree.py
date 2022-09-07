import sys
import psycopg2

#Função para conectar ao banco de dados e criar a tabela no postgree

def conectar_postgree(tabela):

    try:
        con = psycopg2.connect("dbname='docker' user='docker' host='172.17.0.1' port='5432' password='docker'")
        print("Conexão Realizada")
    except psycopg2.DatabaseError:
        sys.exit('Failed to connect to database')

    cursor = con.cursor()

    print("Recriando tabela no banco de dados")
    cursor.execute(f"""
        CREATE TABLE if not exists {tabela} (
	        product varchar NULL,
            created_at varchar NULL,
            uf varchar NULL,
            unit varchar NULL,
            volume float8 NULL,
            year_month date NULL);
        
        TRUNCATE TABLE {tabela};
     """
    )

    con.commit()

    print("Inserindo os dados no csv na tabela criada")
    with open(f'./dados/dados_finais/' + tabela + '.csv') as f:
        cursor.copy_expert(f'COPY {tabela} FROM STDIN WITH HEADER CSV', f)

    con.commit()
    con.close()


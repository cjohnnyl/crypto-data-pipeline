from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import json
import os

# Configurações Padrão da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Caminho onde os dados serão salvos (DENTRO do Container)
# Lembre-se: O volume ./data local está mapeado para /opt/airflow/data no Docker
BASE_PATH = "/opt/airflow/data/bronze"

def fetch_and_save_crypto_data(**kwargs):
    """
    Função que bate na API, pega os dados e salva em JSON.
    """
    # 1. Definição da API
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": "false"
    }

    try:
        # 2. Requisição (Request)
        print(f"Iniciando requisição para {url}...")
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status() # Garante erro se não for 200 OK
        data = response.json()
        print(f"Sucesso! {len(data)} moedas capturadas.")

        # 3. Estrutura de Pastas por Data (Particionamento)
        # Exemplo: /opt/airflow/data/bronze/2023-11-20/
        execution_date = kwargs['ds'] # Data de execução do Airflow (yyyy-mm-dd)
        output_dir = os.path.join(BASE_PATH, execution_date)
        os.makedirs(output_dir, exist_ok=True)

        # 4. Nome do Arquivo com Timestamp
        timestamp = datetime.now().strftime("%H%M%S")
        filename = f"crypto_market_{timestamp}.json"
        file_path = os.path.join(output_dir, filename)

        # 5. Salvar no Disco
        with open(file_path, 'w') as f:
            json.dump(data, f)
        
        print(f"Arquivo salvo em: {file_path}")

    except Exception as e:
        print(f"Erro na ingestão: {e}")
        raise e

# Definição da DAG
with DAG(
    '01_crypto_ingestion_bronze', # ID Único da DAG
    default_args=default_args,
    description='Ingere dados da CoinGecko API para camada Bronze',
    schedule_interval=timedelta(minutes=30), # Roda a cada 30 min
    catchup=False, # Não tenta rodar o passado se você desligar o PC
    tags=['bronze', 'ingestion', 'api'],
) as dag:

    ingest_task = PythonOperator(
        task_id='fetch_coingecko_data',
        python_callable=fetch_and_save_crypto_data,
        provide_context=True # Permite usar kwargs['ds']
    )

    ingest_task
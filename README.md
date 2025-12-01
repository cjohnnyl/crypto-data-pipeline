# 🪙 Crypto Data Pipeline

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Airflow-2.7-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-Core-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-3.0+-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)

### 📖 Sobre o Projeto

O **Crypto Data Pipeline** é uma solução *end-to-end* de Engenharia de Dados desenvolvida para extrair, processar e analisar a volatilidade do mercado de criptomoedas.

O objetivo deste projeto é demonstrar a implementação de uma **Arquitetura de Lakehouse Moderna** (Medallion Architecture) utilizando ferramentas *open source* e padrões de mercado, simulando um ambiente de produção escalável e resiliente.

---

### 🏗 Arquitetura & Tech Stack

O pipeline segue o fluxo **ELT (Extract, Load, Transform)**, garantindo a separação entre processamento e armazenamento.

| Camada | Tecnologia | Função |
| :--- | :--- | :--- |
| **Orquestração** | **Apache Airflow** | Gerenciamento de DAGs, dependências e monitoramento de falhas. |
| **Ingestão** | **Python (Requests)** | Extração de dados da API pública (CoinGecko). |
| **Processamento** | **PySpark** | Processamento distribuído e conversão de formatos (JSON -> Parquet). |
| **Armazenamento** | **Data Lake Local** | Estrutura de diretórios simulando S3 (Bronze, Silver, Gold). |
| **Transformação** | **dbt Core** | Modelagem dimensional, testes de qualidade (Data Quality) e documentação. |
| **Infraestrutura** | **Docker** | Containerização de todos os serviços. |

---

### 📂 Estrutura do Repositório

```text
crypto-data-pipeline/
├── airflow/
│   ├── dags/             # Pipelines de Orquestração (ETL)
│   └── scripts/          # Scripts auxiliares (PySpark/Python)
├── data/                 # Data Lake Local (Simulação S3)
│   ├── bronze/           # Raw Data (JSON)
│   ├── silver/           # Cleaned Data (Parquet)
│   └── gold/             # Business Aggregates
├── dbt_project/          # Transformações SQL e Testes
├── docker-compose.yml    # Infraestrutura como Código
└── requirements.txt      # Dependências Python
# USAR PYTHON 3.10 (Padrão ouro de estabilidade para Airflow+Spark)
FROM apache/airflow:2.9.2-python3.10

USER root

# Instalar OpenJDK-17 (Compatível com Spark atual)
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk-headless && \
    apt-get clean;

# Definir JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64

USER airflow

# Copiar requirements
COPY requirements.txt /requirements.txt

# --- A CORREÇÃO ---
# Agora usamos a constraint correta para Python 3.10
RUN pip install --no-cache-dir -r /requirements.txt \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.2/constraints-3.10.txt"
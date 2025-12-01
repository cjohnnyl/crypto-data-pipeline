FROM apache/airflow:2.7.1

USER root

# Instala OpenJDK-11 (Necessário para o PySpark rodar)
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk-headless && \
    apt-get clean;

# Define a variável JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

USER airflow

# Copia o requirements.txt e instala as dependências
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
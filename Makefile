# Makefile para automatizar o setup do Crypto Data Pipeline
# Usa comandos Docker padrão (genérico para todos os SOs)

.PHONY: up down clean logs ps

up:
	@echo "Configurando ambiente..."
	@echo "AIRFLOW_UID=50000" > .env
	@mkdir -p airflow/logs airflow/plugins airflow/dags data/bronze dbt_project/logs scripts
	@chmod -R 777 airflow data dbt_project scripts 2>/dev/null || true
	@echo "Iniciando Containers..."
	docker compose up -d --build

down:
	@echo "Parando Containers..."
	docker compose down

clean:
	@echo "Limpando tudo (volumes e containers)..."
	docker compose down --volumes --remove-orphans
	@rm -rf airflow/logs/* 2>/dev/null || true

logs:
	@echo "Exibindo logs..."
	docker compose logs -f

ps:
	@echo "Status dos Containers:"
	docker ps
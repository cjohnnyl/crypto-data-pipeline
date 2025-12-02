# Configuração do Projeto - Crypto Data Pipeline

## ✅ Projeto Configurado para Ser Genérico

Este projeto foi configurado para funcionar em **qualquer sistema operacional** usando comandos Docker padrão.

### 📋 Arquivos Principais

1. **`Makefile`** - Comandos automatizados com detecção de `docker-compose` vs `docker compose`
2. **`docker-compose.yml`** - Orquestração usando sintaxe padrão Docker Compose (sem version obsoleta)
3. **`.env`** - Variáveis de ambiente com `AIRFLOW_UID=50000` (genérico para todos os SOs)
4. **`Dockerfile`** - Imagem customizada do Airflow com PySpark

### 🔧 Compatibilidade

#### ✅ Funciona em:
- Docker Desktop (Windows/macOS/Linux)
- Docker Engine (Linux)
- Lima + Nerdctl (macOS/Linux)
- Rancher Desktop
- Colima
- Podman (com alias docker=podman)

#### 💡 Para Lima/Nerdctl (seu caso):

No seu sistema, o comando `docker` é um alias para `lima nerdctl`. 
O Makefile detecta automaticamente e usa o comando correto.

**Se o make não funcionar**, você pode criar um alias no seu `.zshrc`:

```bash
echo 'alias docker="lima nerdctl"' >> ~/.zshrc
echo 'alias docker-compose="lima nerdctl compose"' >> ~/.zshrc
source ~/.zshrc
```

Ou executar diretamente:
```bash
lima nerdctl compose up -d --build
```

### 🚀 Comandos Disponíveis

```bash
# Iniciar (cria .env, diretórios e sobe containers)
make up

# Parar containers (mantém volumes)
make down

# Limpar tudo (remove volumes e dados)
make clean

# Ver logs em tempo real
make logs
```

### 📁 Estrutura de Permissões

O projeto usa `AIRFLOW_UID=50000` (valor padrão Airflow) que funciona em:
- Linux: usuário airflow nos containers
- macOS: mapeamento automático com permissões 777
- Windows: permissões gerenciadas pelo Docker Desktop

### ⚠️ Troubleshooting

**Erro: "Read-only file system"**
```bash
chmod -R 777 airflow data dbt_project scripts
```

**Erro: "docker: command not found" (Lima/Nerdctl)**
```bash
# Use diretamente:
lima nerdctl compose up -d --build

# Ou crie os aliases mencionados acima
```

**Erro: "version is obsolete"**
- ✅ Já corrigido! Removemos `version: '3.4'` do docker-compose.yml

### 🌐 Acesso ao Airflow

Após `make up` (aguarde ~2 minutos):
- URL: http://localhost:8080
- Usuário: `airflow`
- Senha: `airflow`

### 📝 Notas Importantes

1. **Projeto 100% Genérico**: Todos os comandos são Docker padrão
2. **Sem Hardcoding**: Não há caminhos ou comandos específicos de um SO
3. **Portabilidade**: Clone e execute em qualquer máquina com Docker
4. **Documentação**: README.md contém instruções para Windows/Linux/macOS

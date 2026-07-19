# Cloud Intelligence Weekly 🚀

Este projeto automatiza a mineração, filtragem e compilação diária de novidades de arquitetura, atualizações de infraestrutura e segurança das principais tecnologias e provedores de nuvem do mercado. 

Os dados brutos coletados servem como insumo para modelos de IA generativa (Claude) gerarem relatórios executivos e analíticos semanais sob a ótica de um Arquiteto de Infraestrutura Sênior, focando no mercado brasileiro.

---

## 🛠️ Arquitetura do Projeto

O ecossistema é composto por três pilares principais:

```text
Cloud-Intelligence-Weekly/
├── .github/workflows/
│   └── github_actions.yml      # Robô de automação (Cron diário às 3h BRT)
├── prompts/
│   ├── weekly.md               # Prompt estruturado para relatório analítico
│   └── linkedin.md             # Prompt para geração de conteúdo técnico
├── python/
│   └── collector.py            # Script minerador de Feeds RSS oficiais
├── reports/
│   └── raw_daily.md            # Banco de dados bruto em Markdown (UTF-8)
└── requirements.txt            # Dependências do motor Python

🛰️ Fontes Monitoradas de Forma Nativa
O pipeline realiza a extração e validação delta temporal de feeds oficiais de engenharia e core:

AWS: Amazon Web Services Blog (Focado em lançamentos core, atualizações de segurança e IA).

Kubernetes: Blog oficial da comunidade (Arquitetura, depreciações de APIs e ecossistema CNCF).

PostgreSQL: Comunidade Global de Desenvolvimento (Novas versões, betas e ferramentas de ecossistema como poolers e extensions).

🤖 Pipeline de Automação (CI/CD)
A automação em nuvem roda utilizando GitHub Actions com a seguinte lógica:

Gatilho Temporal: Executado automaticamente via expressão Cron todos os dias às 03:00 AM (Horário de Brasília).

Mecanismo Anti-Vazio (Fallback): Caso um provedor não publique artigos técnicos nas últimas 24 horas (comum em fins de semana), o script automaticamente captura os 3 últimos posts gerais para fins de integridade.

Commit Automatizado: Os novos dados minerados são limpos, codificados estritamente em UTF-8 nativo para evitar quebras de caracteres, e salvos diretamente na pasta reports/raw_daily.md pelo robô.

📋 Como Utilizar no Dia a Dia (Geração de Relatórios)
Para extrair a inteligência de nuvem com IA ao final de cada ciclo semanal:

Acesse o arquivo prompts/weekly.md e copie todo o seu conteúdo.

Abra o projeto estruturado no Claude.

Cole o conteúdo do prompt e, logo abaixo (na mesma mensagem), copie e cole o conteúdo acumulado no arquivo reports/raw_daily.md.

O modelo interpretará os dados sob a persona de Arquiteto Sênior, removendo ruídos de marketing e aplicando o filtro de conformidade (custos em dólar, LGPD e impactos práticos de SysAdmin/DevOps).

💻 Desenvolvimento Local
Se precisar rodar, testar ou debugar o minerador na sua máquina:

Pré-requisitos
Python 3.12+ instalado.

Git configurado no terminal.

Configuração e Execução

# Clone o repositório
git clone [https://github.com/claudiomiromarques/Cloud-Intelligence-Weekly.git](https://github.com/claudiomiromarques/Cloud-Intelligence-Weekly.git)
cd Cloud-Intelligence-Weekly

# Instale as dependências
pip install -r requirements.txt

# Execute o coletor localmente
python python/collector.py

# Visualizar a saída corrigida no PowerShell sem quebra de encoding
Get-Content reports/raw_daily.md -Encoding utf8

Mantido de forma automatizada por GitHub Actions.

---

### 📦 Como atualizar no seu GitHub:
Para salvar esse README bonitão no seu repositório remoto, basta rodar esses comandos rápidos no PowerShell:

```powershell
git add README.md
git commit -m "docs: adiciona documentacao completa da arquitetura no readme"
git push origin main
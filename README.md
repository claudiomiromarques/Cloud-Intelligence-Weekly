Aqui está o arquivo completo em um único bloco de código em formato **Markdown (`.md`)**.

Você pode copiar todo o conteúdo dentro do bloco abaixo e colar diretamente no seu arquivo `README.md`:

```markdown
# Cloud Intelligence Weekly 🚀

Este projeto automatiza a mineração, filtragem e compilação diária de novidades de arquitetura, atualizações de infraestrutura, IA, automação e segurança das principais tecnologias e provedores de nuvem do mercado. 

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
│   └── linkedin.md              # Prompt para geração de conteúdo técnico
├── python/
│   └── collector.py            # Script minerador de Feeds RSS oficiais
├── reports/
│   └── raw_daily.md            # Banco de dados bruto em Markdown (UTF-8)
└── requirements.txt            # Dependências do motor Python

```

### 🛰️ Fontes Monitoradas de Forma Nativa

O pipeline realiza a extração e validação delta temporal de feeds RSS/XML categorizados:

| Categoria | Provedor / Ecossistema | Foco de Coleta |
| --- | --- | --- |
| **Cloud** | **AWS** | Lançamentos core, arquitetura e atualizações globais. |
| **Cloud** | **GCP (Google Cloud)** | Produtos GCP, infraestrutura e soluções de nuvem. |
| **Cloud** | **OCI (Oracle Cloud)** | Novidades de OCI, banco de dados e workloads corporativos. |
| **Containers** | **Kubernetes Community** | Arquitetura, depreciação de APIs e ecossistema CNCF. |
| **Database** | **PostgreSQL Global** | Novas versões, notas de patch, extensões e ecossistema. |
| **IaC** | **HashiCorp Terraform** | Provedores, atualizações da HCL e automação de código. |
| **Automation** | **Red Hat Ansible** | Playbooks, automação de infraestrutura e gerenciamento. |
| **IA Generativa** | **Anthropic News (Claude)** | Atualizações de modelos Claude, segurança em IA e pesquisa. |
| **Multicloud** | **The New Stack** | Engenharia, DevOps, cultura cloud-native e tendências. |
| **Segurança** | **Cloudflare Engineering** | Edge computing, mitigação DDoS, DNS e Zero Trust. |
| **HealthTech** | **Governança & LGPD (HIPAA Journal)** | Governança de TI em Saúde, conformidade, privacidade e LGPD. |

---

## 🤖 Pipeline de Automação (CI/CD)

A automação em nuvem roda utilizando GitHub Actions com a seguinte lógica:

1. **Gatilho Temporal:** Executado automaticamente via expressão Cron todos os dias às 03:00 AM (Horário de Brasília).
2. **Mecanismo Anti-Vazio (Fallback):** Caso um provedor não publique artigos técnicos nas últimas 24 horas (comum em fins de semana), o script captura automaticamente os últimos posts gerais para garantir a integridade dos dados.
3. **Commit Automatizado:** Os novos dados minerados são limpos, codificados estritamente em UTF-8 nativo para evitar quebras de caracteres, e salvos diretamente na pasta `reports/raw_daily.md` pelo robô.

---

## 📋 Como Coletar e Usar no Claude (Geração de Relatórios)

Para extrair a inteligência de nuvem com IA ao final de cada ciclo semanal, siga os passos abaixo:

### 1. Limpeza Prévia do Banco de Dados Bruto

Antes de rodar a nova coleta ou ao resetar o ciclo semanal, limpe o arquivo `reports/raw_daily.md`.

> ⚠️ **Atenção ao caminho no PowerShell:** Se o terminal estiver navegado dentro da pasta `prompts/` (`PS C:\...\prompts>`), utilize o caminho relativo subindo um nível (`../`):

```powershell
# Executando a partir do subdiretório /prompts:
Clear-Content -Path "../reports/raw_daily.md" -ErrorAction SilentlyContinue

```

*Se você estiver na **raiz do projeto**, o comando direto é:*

```powershell
# Executando a partir da raiz do projeto:
Clear-Content -Path "reports/raw_daily.md" -ErrorAction SilentlyContinue

```

### 2. Processamento com o Claude

1. Acesse o arquivo `prompts/weekly.md` (ou `prompts/linkedin.md`) e copie todo o seu conteúdo.
2. Abra a conversa no Claude (ou Projeto dedicado).
3. Cole o conteúdo do prompt e, logo abaixo (na mesma mensagem), insira o conteúdo acumulado no arquivo `reports/raw_daily.md`.
4. O modelo interpretará os dados sob a persona de Arquiteto Sênior, removendo ruídos de marketing e aplicando filtros de conformidade (custos em dólar, LGPD/HIPAA e impactos práticos de SysAdmin/DevOps/SRE).

---

## 💻 Desenvolvimento Local

Se precisar rodar, testar ou debugar o minerador na sua máquina:

### Pré-requisitos

* Python 3.12+ instalado.
* Git configurado no terminal.

### Configuração e Execução

```powershell
# Clone o repositório
git clone [https://github.com/claudiomiromarques/Cloud-Intelligence-Weekly.git](https://github.com/claudiomiromarques/Cloud-Intelligence-Weekly.git)
cd Cloud-Intelligence-Weekly

# Instale as dependências
pip install -r requirements.txt

# Execute o coletor localmente
python python/collector.py

# Visualizar a saída no PowerShell garantindo encoding UTF-8
Get-Content reports/raw_daily.md -Encoding utf8

```
---

### 📦 Comandos para salvar e enviar ao GitHub pelo PowerShell:

```
git add ../README.md

git commit -m "docs: atualiza readme com novas fontes e comandos de limpeza"

git push origin main
---

Aqui está o bloco para você adicionar no **`README.md`** explicando como resolver conflitos de sincronização entre o seu ambiente local e as atualizações automáticas do GitHub Actions.

Você pode colar esta seção logo antes da seção final ("Mantido de forma automatizada..."):

```markdown
---

## 🔄 Sincronização Local com o GitHub Actions

Como o robô do GitHub Actions realiza commits automáticos diários diretamente no repositório remoto (atualizando o `reports/raw_daily.md`), o seu ambiente local pode ficar desatualizado em relação ao remoto (`non-fast-forward`).

Caso encontre o erro `[rejected] main -> main (fetch first)` ao tentar dar `git push`, siga o procedimento abaixo:

### 1. Salve suas alterações locais
```powershell

git add .

git commit -m "feat: ATualiza do README"

```

### 2. Sincronize com o repositório remoto

Utilize o `pull` com mesclagem padrão para integrar as atualizações diárias da automação:

```powershell

git pull origin main --no-rebase

```

* 💡 **Em caso de conflito no arquivo `raw_daily.md`:** Aceite a versão local e finalize a mesclagem:
```powershell

git checkout --ours reports/raw_daily.md

git add reports/raw_daily.md

git commit -m "fix: resolve conflito no raw_daily.md"

```

### 3. Envie as atualizações

```powershell

git push origin main

```

```

```

Mantido de forma automatizada por GitHub Actions.

```

```
# Cloud Intelligence Weekly - Relatório Semanal

**Nota metodológica:** os dados brutos desta semana são bem mais enxutos do que o normal — não há nenhuma novidade capturada para **Azure, OCI ou GCP**, e as categorias AWS/Kubernetes/PostgreSQL vieram majoritariamente do "feed geral" por falta de eventos nas últimas 24h. Apliquei o filtro rigoroso pedido (fora marketing e lançamentos estéticos), o que reduziu ainda mais o volume de itens elegíveis. Prefiro reportar isso com transparência a inflar o relatório com itens de baixo valor.

---

## 📌 Visão Geral e Tendências

**Top 5 Tendências da Semana:**
1. **Consolidação de ferramentas de gestão no Kubernetes** — migração de Kubernetes Dashboard para Headlamp ganha tração oficial, sinalizando mudança de padrão de observabilidade de cluster.
2. **Kubernetes como plataforma padrão para AI/ML** — novo plugin Headlamp para Kubeflow reforça o cluster K8s como base operacional para workloads de IA.
3. **Observabilidade orientada a métricas de negócio** — guia oficial de exporter de métricas customizadas mostra o afastamento do modelo "CPU/memória apenas" para autoscaling.
4. **Antecipação do ciclo PostgreSQL 19** — Beta 2 liberado, sinalizando maturação do próximo major release.
5. **Ecossistema satélite do Postgres em movimento** — atualizações em connection pooling (Odyssey) e monitoramento (powa-archivist), sem quebras de compatibilidade aparentes.

**Top 5 Novidades de IA para Infra:**
1. Plugin Headlamp para Kubeflow (gestão de workloads de ML em K8s).
2. Menção a **Claude Sonnet 5 disponível na AWS** (roundup semanal da AWS).
3. Menção a **Amazon WorkSpaces para agentes de IA** (roundup semanal da AWS).
4. Exporter de métricas customizadas no K8s — base técnica para autoscaling orientado por sinais de IA/filas de mensagens.
5. *(Sem quinto item de peso nos dados coletados — Azure AI/GCP Vertex/OCI AI ausentes do feed desta semana.)*

---

## ☁️ Ecossistema Cloud & Infraestrutura (Top 5 Novidades)

### Kubernetes Dashboard → Headlamp (guia oficial de migração) - Kubernetes
- **Resumo:** O projeto Kubernetes publicou um guia passo a passo oficial para migrar do Dashboard tradicional para o Headlamp, um novo cliente de gestão de cluster.
- **Link Oficial:** https://kubernetes.io/blog/2026/07/13/kubernetes-dashboard-to-headlamp/
- **Vale estudar agora?:** Sim — quando o próprio projeto publica um guia de migração oficial, é sinal de que o Dashboard tradicional está perdendo prioridade de manutenção. Vale testar o Headlamp em ambiente de homologação.
- **Impacto para Empresas Brasileiras:** Baixo custo de adoção (ferramenta open source), sem impacto direto em LGPD/compliance, mas equipes que dependem de scripts/automations em cima do Dashboard antigo devem mapear dependências antes de migrar.
- **Impacto para Profissionais de Infraestrutura:** DevOps/SREs devem revisar runbooks de acesso ao cluster e treinar times de suporte no novo painel antes que o Dashboard antigo seja descontinuado.

### Headlamp Plugin para Kubeflow - Kubernetes / IA
- **Resumo:** Novo plugin permite operar workloads de ML (notebooks, treinamento distribuído, pipelines) diretamente pela interface do Headlamp.
- **Link Oficial:** https://kubernetes.io/blog/2026/07/13/introducing-headlamp-plugin-for-kubeflow/
- **Vale estudar agora?:** Sim, para times que já rodam Kubeflow — reduz fricção operacional. Não é urgente para quem ainda não adotou Kubeflow.
- **Impacto para Empresas Brasileiras:** Reduz necessidade de ferramentas proprietárias de MLOps, o que ajuda a controlar custo em dólar (menos SaaS externo).
- **Impacto para Profissionais de Infraestrutura:** Abre caminho para consolidar observabilidade de infraestrutura + ML em uma única ferramenta, reduzindo context-switching.

### Custom Metrics Exporter para Kubernetes - Kubernetes
- **Resumo:** Artigo técnico oficial detalha como construir exporters de métricas customizadas (tamanho de fila, duração de batch jobs, conexões WebSocket ativas) para autoscaling além de CPU/memória.
- **Link Oficial:** https://kubernetes.io/blog/2026/07/14/custom-metrics-exporter-kubernetes/
- **Vale estudar agora?:** Sim — é conteúdo de boas práticas, não uma feature nova, então tem validade duradoura para arquitetos de autoscaling.
- **Impacto para Empresas Brasileiras:** Ajuda a evitar superprovisionamento (economia direta em dólar em clusters gerenciados na AWS/Azure/GCP).
- **Impacto para Profissionais de Infraestrutura:** Muda a régua de maturidade de HPA/KEDA — arquitetos devem parar de tratar CPU/memória como único sinal de escala.

### AWS Weekly Roundup (Security Hub Network Scanning, Claude Sonnet 5, WorkSpaces para agentes de IA) - AWS
- **Resumo:** Roundup oficial da AWS cita, entre outros itens, a chegada de **Network Scanning no Security Hub** e a disponibilização do **Claude Sonnet 5** e de **WorkSpaces para agentes de IA** na plataforma.
- **Link Oficial:** https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-builder-center-at-one-year-network-scanning-in-security-hub-loom-for-aws-and-more-july-13-2026/
- **Vale estudar agora?:** Parcialmente — Network Scanning em Security Hub merece atenção de times de segurança; os itens de IA são mais estratégicos que operacionais no momento.
- **Impacto para Empresas Brasileiras:** Network Scanning pode reduzir custo de auditoria de exposição de rede, relevante para compliance de segurança sem depender de ferramenta terceira.
- **Impacto para Profissionais de Infraestrutura:** Times de Security/Cloud devem avaliar se o Security Hub já cobre a superfície de rede que hoje é auditada manualmente ou por terceiros.

### *(Lacuna de dados: Azure, OCI e GCP)*
- **Resumo:** Não houve nenhuma publicação nas fontes oficiais monitoradas (Azure Blog, GCP Blog, Oracle Cloud Infrastructure Blog) nas últimas 24h/7 dias no dataset fornecido.
- **Recomendação:** Verificar manualmente https://azure.microsoft.com/blog/ , https://cloud.google.com/blog/ e https://blogs.oracle.com/cloud-infrastructure/ na próxima coleta para não perder eventos relevantes desses provedores.

---

## 🔒 Segurança & Open Source (Top 5 Novidades)

### PostgreSQL 19 Beta 2 - PostgreSQL
- **Resumo:** O PostgreSQL Global Development Group lançou a segunda beta da versão 19, com previews de features antes do lançamento geral.
- **Link Oficial:** https://www.postgresql.org/about/news/postgresql-19-beta-2-released-3350/
- **Vale estudar agora?:** Sim, em ambiente de teste — nunca em produção. Times que dependem de features novas devem começar a validar compatibilidade agora.
- **Impacto para Empresas Brasileiras:** Nenhum impacto imediato de custo; janela boa para planejar upgrade sem pressão de EOL.
- **Impacto para Profissionais de Infraestrutura:** DBAs devem mapear extensões e queries que podem ser afetadas por mudanças de planner/otimizador antes do GA.

### Odyssey 1.5.1 (connection pooler) - PostgreSQL
- **Resumo:** Nova versão do pooler de conexões multi-thread para PostgreSQL e Apache Cloudberry, com correções no suporte a protocolo estendido e ganhos de performance.
- **Link Oficial:** https://www.postgresql.org/about/news/odyssey-151-released-3348/
- **Vale estudar agora?:** Sim, se você já usa Odyssey em produção — correções de protocolo podem resolver bugs sutis de conexão.
- **Impacto para Empresas Brasileiras:** Redução de custo operacional via menor número de conexões físicas ao banco, especialmente relevante em bancos gerenciados cobrados por conexão.
- **Impacto para Profissionais de Infraestrutura:** Vale aplicar o patch em homologação antes de produção, checando changelog completo de correções de protocolo.

### powa-archivist 5.2.0 - PostgreSQL (monitoramento)
- **Resumo:** Nova versão da extensão core do projeto PoWA (Postgres Workload Analyzer).
- **Link Oficial:** https://www.postgresql.org/about/news/powa-archivist-520-is-out-3347/
- **Vale estudar agora?:** Baixa prioridade — é atualização incremental de ferramenta de monitoramento, sem mudança arquitetural.
- **Impacto para Empresas Brasileiras:** Nenhum impacto financeiro relevante.
- **Impacto para Profissionais de Infraestrutura:** Apenas atualizar se já usa PoWA; revisar release notes por mudanças de schema de coleta.

### *(Sem itens de Docker/Linux/Segurança dedicados nesta coleta)*
- **Observação:** O dataset não trouxe publicações específicas de segurança crítica (CVE), Docker ou distribuições Linux nesta janela. Recomendo cruzar com https://blog.cloudflare.com/ e https://www.redhat.com/en/blog na próxima rodada de coleta.

### AWS Security Hub – Network Scanning (repetição por relevância de segurança) - AWS/Segurança
- **Resumo:** Já descrito acima — nova capacidade de varredura de rede dentro do Security Hub.
- **Link Oficial:** https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-builder-center-at-one-year-network-scanning-in-security-hub-loom-for-aws-and-more-july-13-2026/
- **Vale estudar agora?:** Sim, times de segurança em nuvem devem avaliar cobertura versus scanners externos (Qualys, Tenable etc.).
- **Impacto para Profissionais de Infraestrutura:** Potencial simplificação de stack de segurança, com consolidação de ferramentas nativas AWS.

---

## ✍️ Opinião do Arquiteto (Fatos Relevantes)

**1. A migração Dashboard → Headlamp é mais sintoma do que causa.** Em projetos reais, já vi times resistirem a trocar ferramentas de gestão de cluster por puro hábito, mesmo quando a ferramenta antiga está em modo de manutenção mínima. O risco de adoção precoce aqui é baixo — Headlamp já tem maturidade suficiente — mas o risco real é operacional: scripts internos, RBAC customizado e integrações de SSO feitas em cima do Dashboard antigo tendem a ser mal documentados. Recomendo tratar essa migração como um mini-projeto com inventário de dependências, não como troca de "só trocar a URL".

**2. Kubernetes virando a plataforma default de MLOps é uma tendência que já passou do ponto de ser opcional.** O plugin Kubeflow no Headlamp confirma isso. O ganho de performance real não vem da ferramenta em si, mas de unificar observabilidade de infra e de ML — hoje muitas empresas mantêm dashboards separados para GPU/nó e para job de treinamento, o que atrasa troubleshooting em incidentes. O risco de adoção precoce é subestimar a curva de aprendizado de times de infra tradicionais com conceitos de ML pipeline; vale investir em treinamento cruzado antes de migrar workloads críticos.

**3. O ciclo de vida do PostgreSQL 19 (Beta 2) e o movimento do ecossistema satélite (Odyssey, PoWA) mostram uma coisa que costuma ser subestimada: a maturidade do Postgres hoje não está mais só no core, está no ecossistema em volta.** Para empresas brasileiras que migram de bancos proprietários para Postgres visando redução de custo em dólar, o conselho real de campo é: não espere o GA da v19 para começar a testar — comece agora em homologação, porque historicamente as primeiras minor releases pós-GA carregam correções de regressões de planner que pegam quem só testa em produção.

---

**Resumo do gap de dados:** para a próxima coleta, sugiro reforçar a captura de Azure, GCP e OCI, já que esta semana o relatório ficou desbalanceado a favor de Kubernetes/PostgreSQL simplesmente por ausência de sinal dos outros provedores — não porque eles estejam parados.
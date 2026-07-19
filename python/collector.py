import feedparser
import datetime
import os

FEEDS = {
    "AWS": "https://aws.amazon.com/blogs/aws/feed/",
    "Kubernetes": "https://kubernetes.io/feed.xml",
    "PostgreSQL": "https://www.postgresql.org/news.rss"
}

def collect_news():
    now = datetime.datetime.now(datetime.timezone.utc)
    yesterday = now - datetime.timedelta(days=1)
    
    content = "# Dados Brutos Coletados nas Últimas 24h\n\n"
    
    for category, url in FEEDS.items():
        feed = feedparser.parse(url)
        content += f"## Categoria: {category}\n"
        
        has_news = False
        # Passo 1: Tentar coletar dados das últimas 24h
        for entry in feed.entries:
            published_parsed = entry.get("published_parsed")
            if published_parsed:
                pub_date = datetime.datetime(*published_parsed[:6], tzinfo=datetime.timezone.utc)
                if pub_date > yesterday:
                    content += f"### Título: {entry.title}\n"
                    content += f"- Link: {entry.link}\n"
                    content += f"- Resumo Original: {entry.summary[:300]}...\n\n"
                    has_news = True
        
        # Passo 2: Se for fim de semana/sem notícias, pegar os 3 últimos posts como demonstração
        if not has_news and len(feed.entries) > 0:
            content += "*(Sem novidades nas últimas 24h. Mostrando últimas publicações gerais do feed:)*\n\n"
            for entry in feed.entries[:3]:
                content += f"### Título: {entry.title}\n"
                content += f"- Link: {entry.link}\n"
                content += f"- Resumo Original: {entry.summary[:300]}...\n\n"
                    
    os.makedirs("reports", exist_ok=True)
    # Gravando explicitamente em utf-8
    with open("reports/raw_daily.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("Coleta diária finalizada com sucesso!")

if __name__ == "__main__":
    collect_news()

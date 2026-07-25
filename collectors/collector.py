import os
import xml.etree.ElementTree as ET
import requests
import yaml
import time
import re
from datetime import datetime

def load_sources():
    config_path = os.path.join("config", "sources.yaml")
    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def fetch_rss_feed(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1'
        }
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            return response.content
        else:
            print(f"❌ Erro HTTP {response.status_code} ao acessar {url}")
            return None
    except Exception as e:
        print(f"❌ Erro de rede ao baixar o feed {url}: {e}")
        return None

def sanitize_xml(xml_text):
    xml_text = xml_text.replace('&nbsp;', ' ').replace('&ldquo;', '"').replace('&rdquo;', '"')
    xml_text = re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;|#[0-9]+;)', '&amp;', xml_text)
    xml_text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', xml_text)
    return xml_text

def fallback_regex_parser(xml_text, provider_name, category):
    articles = []
    titles = re.findall(r'<title.*?>(.*?)</title>', xml_text, re.DOTALL)[:4]
    links = re.findall(r'href="(https://.*?)"', xml_text)[:4]
    
    if not links:
        links = re.findall(r'<link.*?>(.*?)</link>', xml_text, re.DOTALL)[:4]

    start_idx = 1 if len(titles) > 1 and provider_name.lower() in titles[0].lower() else 0
    for t, l in zip(titles[start_idx:start_idx+3], links[start_idx:start_idx+3]):
        clean_t = re.sub('<[^<]+?>', '', t).strip()
        clean_l = l.strip()
        if clean_t and clean_l and "css" not in clean_l and "js" not in clean_l:
            articles.append(f"- **[{category}]** {clean_t} ({provider_name})\n  Link: {clean_l}")
            
    return articles

def parse_feed(xml_data, provider_name, category):
    if not xml_data:
        return []
    
    try:
        xml_text = xml_data.decode('utf-8', errors='ignore').strip()
        
        if "<html" in xml_text.lower() or "doctype html" in xml_text.lower():
            return fallback_regex_parser(xml_text, provider_name, category)
            
        xml_text = sanitize_xml(xml_text)
        root = ET.fromstring(xml_text)
        articles = []
        
        items = root.findall('.//item')
        if items:
            for item in items[:3]:
                title_node = item.find('title')
                link_node = item.find('link')
                title = title_node.text.strip() if title_node is not None and title_node.text else "Sem título"
                link = link_node.text.strip() if link_node is not None and link_node.text else ""
                articles.append(f"- **[{category}]** {title} ({provider_name})\n  Link: {link}")
            return articles
        else:
            namespaces = {'atom': 'http://www.w3.org/2005/Atom'}
            entries = root.findall('.//atom:entry', namespaces) or root.findall('.//entry')
            for entry in entries[:3]:
                # Correção estrita da validação de nós (Silencia o DeprecationWarning do Python 3.12+)
                title_node = entry.find('atom:title', namespaces)
                if title_node is None:
                    title_node = entry.find('title')
                title = title_node.text.strip() if title_node is not None and title_node.text else "Sem título"
                
                link_node = entry.find('atom:link', namespaces)
                if link_node is None:
                    link_node = entry.find('link')
                
                link = ""
                if link_node is not None:
                    link = link_node.attrib.get('href', '').strip() if 'href' in link_node.attrib else (link_node.text or "")
                articles.append(f"- **[{category}]** {title} ({provider_name})\n  Link: {link}")
            return articles
            
    except Exception as e:
        return fallback_regex_parser(xml_text, provider_name, category)

def main():
    print("🚀 Inicializando o Cloud Intelligence Collector Sênior Pro V3...")
    sources = load_sources()
    
    os.makedirs("reports", exist_ok=True)
    report_path = os.path.join("reports", "raw_daily.md")
    
    today_str = datetime.now().strftime("%d/%m/%Y")
    output_content = [f"### 🗓️ Coleta de Dados Brutos - {today_str}\n"]
    
    for key, info in sources['providers'].items():
        print(f"📡 Minerando: {info['name']}...")
        xml_data = fetch_rss_feed(info['feed_url'])
        articles = parse_feed(xml_data, info['name'], info['category'])
        
        if articles:
            output_content.extend(articles)
            output_content.append("") 
        else:
            output_content.append(f"- **[{info['category']}]** Sem atualizações disponíveis para {info['name']}.")
        
        time.sleep(2.0)
            
    with open(report_path, "a", encoding="utf-8") as file:
        file.write("\n".join(output_content) + "\n---\n")
    
    print(f"✅ Execução concluída. Resultados salvos em: {report_path}")

if __name__ == "__main__":
    main()

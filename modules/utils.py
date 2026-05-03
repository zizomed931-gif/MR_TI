import requests, re, random, socket

def get_header():
    agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6)"]
    return {'User-Agent': random.choice(agents)}

def scan_sql(target):
    payload = "'"
    try:
        res = requests.get(f"http://{target}/index.php?id={payload}", headers=get_header(), timeout=5)
        if "sql syntax" in res.text.lower():
            return f"⚠️ مصاب بـ SQL Injection (Payload: {payload})"
        return "✅ آمن من SQL الشائع"
    except: return "❌ تعذر الفحص"

def scrape_info(target):
    try:
        res = requests.get(f"http://{target}", headers=get_header(), timeout=5)
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", res.text)
        return list(set(emails))[:5]
    except: return []

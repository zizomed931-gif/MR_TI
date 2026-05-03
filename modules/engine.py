import requests
import socket

def run_scan(target):
    try:
        ip = socket.gethostbyname(target)
        res = requests.get(f"http://{target}", timeout=5)
        headers = res.headers
        vulns = []
        if 'X-Frame-Options' not in headers: vulns.append("Missing X-Frame-Options")
        if 'Server' in headers: vulns.append(f"Server: {headers['Server']}")
        
        return {"target": target, "ip": ip, "vulns": ", ".join(vulns)}
    except:
        return None

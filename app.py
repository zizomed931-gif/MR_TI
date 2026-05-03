from flask import Flask
from modules.database import get_all_results

app = Flask(__name__)

@app.route('/')
def index():
    data = get_all_results()
    html = "<h1>M.R. TI Dashboard</h1><table border='1'><tr><th>Target</th><th>IP</th><th>Vulnerabilities</th></tr>"
    for row in data:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
    html += "</table>"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

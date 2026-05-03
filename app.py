from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('database/mrti.db')
    rows = conn.execute('SELECT * FROM results').fetchall()
    conn.close()
    html = """
    <body style="background:#111; color:#0f0; font-family:sans-serif; padding:50px;">
        <h1>📊 لوحة تحكم M.R. TI</h1>
        <table border="1" style="width:100%; text-align:left;">
            <tr><th>الهدف</th><th>IP</th><th>الحالة</th></tr>
            {% for row in rows %}
            <tr><td>{{row[0]}}</td><td>{{row[1]}}</td><td>{{row[2]}}</td></tr>
            {% endfor %}
        </table>
    </body>
    """
    return render_template_string(html, rows=rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

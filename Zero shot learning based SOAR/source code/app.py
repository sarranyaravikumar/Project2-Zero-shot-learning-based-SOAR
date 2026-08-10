from flask import Flask, render_template,request
from fetch_logs import fetch_logs
from detector import detect
from block import block_ip
import time

app = Flask(__name__)
blocked_ips = set()
data = []
WHITELIST = ["10.111.251.222"]
def monitor():
    while True:
        logs = fetch_logs()

        for log in logs:
            if not log.strip():
                continue

            print("Processing:", log)

            try:
                ip, attack, score = detect(log)
            except:
                continue

            status = "Benign"

            if attack != "Normal Traffic":
                if ip not in WHITELIST:
                    block_ip(ip)
                status = "Blocked 🚫"
            else:
                status="Benign"

            data.append({
                "ip": ip,
                "attack": attack,
                "score": round(score, 2),
                "status": status
            })

        time.sleep(5)   # ✅ INSIDE loop

@app.route("/")
def index():
    user_ip = request.remote_addr
    print("User IP:", user_ip)
    print("Blocked IPs:", blocked_ips)
    if user_ip in blocked_ips:
        return render_template("blocked.html")

    return render_template("index.html", logs=data[-20:])

if __name__ == "__main__":
    import threading
    t = threading.Thread(target=monitor)
    t.daemon = True
    t.start()

    app.run(port=5000)
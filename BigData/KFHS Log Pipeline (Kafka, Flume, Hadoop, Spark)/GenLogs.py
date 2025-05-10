
import time
import random
from datetime import datetime

# Sample data
ips = ["127.0.0.1", "192.168.1.10", "10.0.0.5"]
urls = ["/", "/index.html", "/about", "/contact", "/login"]
methods = ["GET", "POST"]
statuses = [200, 404, 500, 302]
agents = ["curl/7.68.0", "Mozilla/5.0", "PostmanRuntime/7.28.0"]

# Output file path
log_file = "/home/bigdata/Desktop/fake_nginx_access.log"

def generate_log():
    ip = random.choice(ips)
    time_str = datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")
    method = random.choice(methods)
    url = random.choice(urls)
    status = random.choice(statuses)
    size = random.randint(100, 5000)
    agent = random.choice(agents)

    return f'{ip} - - [{time_str}] "{method} {url} HTTP/1.1" {status} {size} "-" "{agent}"\n'

# Stream logs every second
with open(log_file, "a") as f:
    while True:
        log_line = generate_log()
        f.write(log_line)
        f.flush()  # Force write to disk
        print(log_line.strip())  # Also print to console
        time.sleep(10)

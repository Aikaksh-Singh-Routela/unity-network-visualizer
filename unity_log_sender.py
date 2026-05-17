"""
Unity Log Sender - Sends network logs to Unity via UDP
"""

import socket
import random
import time
import json
from datetime import datetime

# Malicious IPs (known bad actors)
malicious_ips = [
    "185.142.53.35", "45.155.205.233", "194.87.237.5",
    "5.188.87.45", "185.130.5.253", "94.102.61.78"
]

normal_external = [
    "8.8.8.8", "8.8.4.4", "1.1.1.1", "142.250.185.46"
]

# Unity IP and port (Unity will listen on this port)
UNITY_IP = "127.0.0.1"
UNITY_PORT = 5005

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def generate_log():
    """Generate a single log entry"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    protocol = random.choice(["TCP", "UDP"])

    # 30% chance of suspicious activity
    is_suspicious = random.random() < 0.3

    if is_suspicious:
        src = f"192.168.1.{random.randint(1, 50)}"
        dst = random.choice(malicious_ips)
        port = random.choice([22, 23, 3389, 445, 1433])
        flag = random.choice(["SYN", "RST"])
        threat_type = random.choice(["Ransomware", "DDoS", "Port Scan", "Brute Force"])
    else:
        src = f"192.168.1.{random.randint(1, 50)}"
        dst = random.choice(normal_external)
        port = random.choice([80, 443, 53])
        flag = "ACK"
        threat_type = "Normal"

    log = {
        'timestamp': timestamp,
        'protocol': protocol,
        'source_ip': src,
        'source_port': random.randint(1024, 65535),
        'dest_ip': dst,
        'dest_port': port,
        'flag': flag,
        'is_suspicious': is_suspicious,
        'threat_type': threat_type,
        'message': f"{timestamp} {protocol} {src}:{random.randint(1024, 65535)} → {dst}:{port} FLAG: {flag}"
    }
    return log


def send_log_to_unity(log):
    """Send log to Unity via UDP"""
    message = json.dumps(log)
    sock.sendto(message.encode(), (UNITY_IP, UNITY_PORT))
    print(f"📤 Sent: {log['threat_type']} - {log['dest_ip']}")


print("🚀 Unity Log Sender Started")
print(f"Sending logs to {UNITY_IP}:{UNITY_PORT}")
print("Press Ctrl+C to stop\n")

try:
    count = 0
    while True:
        log = generate_log()
        send_log_to_unity(log)
        count += 1
        if count % 10 == 0:
            print(f"📊 Sent {count} logs total")
        time.sleep(1)  # 1 log per second
except KeyboardInterrupt:
    print(f"\n✅ Stopped. Total logs sent: {count}")
    sock.close()
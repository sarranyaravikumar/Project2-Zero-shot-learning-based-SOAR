import paramiko

def block_ip(ip):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect("10.111.251.19", username="sarra", password="123")

        cmd = f"sudo iptables -A INPUT -s {ip} -j DROP"
        stdin, stdout, stderr = ssh.exec_command(cmd)

        print("OUTPUT:", stdout.read().decode())
        print("ERROR:", stderr.read().decode())

        ssh.close()

        print(f"Blocked IP: {ip}")

    except Exception as e:
        print("Blocking failed:", e)
import paramiko

HOST = "10.111.251.19"
USER = "sarra"
PASS = "123"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PASS)

def fetch_logs():
    stdin, stdout, stderr = ssh.exec_command("tail -n 10 /var/log/apache2/access.log")
    output = stdout.read().decode()
    return output.split("\n")
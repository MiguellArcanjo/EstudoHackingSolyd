import paramiko

host = "127.0.0.1"
user = "..."
passwd = "..."

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)
stdin, stout, stderr = client.exec_command("ls")
print(stout.readlines())
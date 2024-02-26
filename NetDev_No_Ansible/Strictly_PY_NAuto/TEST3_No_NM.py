import subprocess

def ssh_command(username, password, hostname, port, command):
    ssh_process = subprocess.Popen(['sshpass', '-p', password, 'ssh', '-o', 'StrictHostKeyChecking=no', '-p', str(port), f'{username}@{hostname}', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = ssh_process.communicate()
    return stdout, stderr

# Example Usage
username = "neteng"
password = "neteng"
hostname = "192.168.39.50"
port = 22  # Default SSH port
command = "show ip int bri"

stdout, stderr = ssh_command(username, password, hostname, port, command)
if stdout:
    print("Command output:")
    print(stdout)
if stderr:
    print("Error occurred:")
    print(stderr)

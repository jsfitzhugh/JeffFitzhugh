from paramiko import SSHClient
from paramiko.client import AutoAddPolicy


# Fill in IP, username info, and command to execute

def main():
    with SSHClient() as client:
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect('0.0.0.0', username='username', password='password')
        stdin, stdout, stderr = client.exec_command('insert command here')
        output = (stdout.read())
        print(output.decode())


if __name__ == '__main__':
    main()

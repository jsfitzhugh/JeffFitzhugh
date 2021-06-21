from paramiko import SSHClient
from paramiko.client import AutoAddPolicy
import stdiomask
# prompts for username and password for remote host

uname = input('Username: ')
pwd = input('Password: ')

cmd = 'ls; ls -l; netstat -t'

print('Please wait, connecting to remote host...')


def main():
    with SSHClient() as client:
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect('192.168.0.8', username=uname, password=pwd)
        stdin, stdout, stderr = client.exec_command(cmd)
        output = (stdout.read())
        print(output.decode())
        print('***Operation Completed***')


if __name__ == '__main__':
    main()

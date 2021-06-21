import subprocess
import platform


def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '5', host]
    return subprocess.call(command)


host = '192.168.0.1'
print(ping(host))

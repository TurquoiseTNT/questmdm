import subprocess

ADB_PATH = 'adb'


def run(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip() + "\n" + result.stderr.strip()

def list_devices():
    output = run([ADB_PATH, 'devices'])
    devices = []
    for line in output.splitlines():
        if '\tdevice' in line:
            serial = line.split('\t')[0]
            devices.append(serial)
    return devices

def connect_device(serial, ip):
    run([ADB_PATH, '-s', serial, 'tcpip', '5555'])
    run([ADB_PATH, 'connect', ip])
    run([ADB_PATH, '-s', serial, 'shell', 'am', 'broadcast', '-a', 'com.questmdm.SETUP_COMPLETE'])
    return "Connected to " + ip

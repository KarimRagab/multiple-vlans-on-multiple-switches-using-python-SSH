  
from netmiko import ConnectHandler

for oct in range (102,106):
    ssh_info = {
    'device_type': 'cisco_ios',
    'username': 'admin',
    'ip' : '192.168.62.' + str(oct),
    'password': 'cisco',
    'secret':   'cisco'
    }
    print("ssh to Host " + str(oct))
    net_connect = ConnectHandler(**ssh_info)
    print("connected")
    for n in ssh_info:
        net_connect.enable()
    for vlan in range (2,30):
        config =['vlan ' + str(vlan)]
        outPut = net_connect.send_config_set(config)
        print(outPut)
    net_connect.disconnect() 
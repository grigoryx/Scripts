#importing the necessary modules
import paramiko
import time

#list of devices
devices = ['10.10.10.1', '192.168.1.1', '172.16.1.1']

#username and (enable) password
username = 'admin'
password = 'cisco123'
enablepass = 'cisco123'

#iterating through the devices
for device in devices:
    #creating an SSH client
    client = paramiko.SSHClient()
    #adding the SSH key
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #connecting to the device
    client.connect(device, username=username, password=password)
    #creating an interactive shell
    shell = client.invoke_shell()
    #sending the enable command
    shell.send('enable\n')
    #waiting for the response
    time.sleep(1)
    #sending the enable password
    shell.send(enablepass + '\n')
    #waiting for the response
    time.sleep(1)
    #sending the write memory command
    shell.send('write memory\n')
    #waiting for the response
    time.sleep(1)
    #closing the connection
    client.close()

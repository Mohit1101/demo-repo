import paramiko

ssh_client = paramiko.SSHClient()
print(type(ssh_client))
print('Connecting to 10.1.1.10')

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname='10.1.1.10',username='u1',password='cisco',port='22',
                   look_for_keys=False ,allow_agent=False)
print('CLosing connection')
ssh_client.close()
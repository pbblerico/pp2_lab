from dataclasses import dataclass
import json 
from sampledata import data_str

data = json.loads(data_str)

print('Interface Status', '=' * 80, sep='\n')
print(f"DN{' ':50}Descrition{' ':10}Speed{' ':3}MTU")
print('-' * 50, '-' * 20, '-' * 6, '-' * 6)
for i in data['imdata']:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    descr = i["l1PhysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]['speed']
    mtu = i["l1PhysIf"]["attributes"]['mtu']
    print(f'{dn:42}{" ":^15}{descr}{" ":14}{speed}{" ":2}{mtu}')

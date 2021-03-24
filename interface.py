from ncclient import manager
from jinja2 import Template
m = manager.connect(host='10.10.20.48', port=830, username='cisco1',password='cisco1', device_params={'name': 'csr'})
# Create a configuration filter
interface_filter = '''
  <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
          <interface>
            <GigabitEthernet>
              <name>1</name>
            </GigabitEthernet>
          </interface>
      </native>
  </filter>
'''

# Execute the get-config RPC
result = m.get_config('running', interface_filter)
print(result)

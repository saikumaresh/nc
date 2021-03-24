from ncclient import manager
import xmltodict
import xml.dom.minidom

host = 'ios-xe-mgmt.cisco.com'
user = 'developer'
password = 'C1sco12345'
port=10000
payload = """
  <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <hostname/>
    </native>
  </filter>
  """

data = '''
  <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <hostname>Sai_kumaresh</hostname>
    </native>
  </config>
'''
get_name=''''
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <username>
          <name/>
        </username>
      </native>
    </filter>
'''

edit_name='''
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <username>
          <name>___sk___</name>
        </username>
      </native>
    </config>
'''
  # Connect to device
def csr_connect(host, port, user, password):
  return manager.connect(host=host,port=port,username=user,password=password,device_params={'name': "csr"},timeout=30)

def get_name(m):
  netconf_reply = m.get(payload).xml
  netconf_dict = xmltodict.parse(netconf_reply)
  hostname = netconf_dict['rpc-reply']['data']['native']['hostname']
  print("Hostname :")
  print(hostname)
  print("\n")
  if(hostname=="csr1000v-1"):
    edit_value(m)


def edit_value(m):
    #xmlDom = xml.dom.minidom.parseString( str( m.edit_config(data, target='running') ) )
    # xpath
    #xmlDom = xml.dom.minidom.parseString( str( m.get_config( source='running', filter=('xpath', '/native/hostname')))) 
    #print (xmlDom.toprettyxml( indent = "  " ))
    m.edit_config(data, target='running')
    print("Name Changed!\n")
    

if __name__ == '__main__':
  with csr_connect(host='10.10.20.48', port=830, user='cisco1', password='cisco1') as m:
    get_name(m)  
    


from ncclient import manager
import xmltodict
import xml.dom.minidom

m = manager.connect(host='10.10.20.48', port=830, username='ciscco1', password='ciscco1',device_params={'name': 'csr'})

ospf="""
<config>
    <native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
			<ospf
				xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
				<id>1</id>
				<network>
					<ip>172.16.100.1</ip>
					<mask>0.0.0.0</mask>
					<area>1</area>
				</network>
				<network>
					<ip>172.16.101.1</ip>
					<mask>0.0.0.0</mask>
					<area>2</area>
				</network>
			</ospf>
		</router>
    </native>
</config>
"""

xmlDom = xml.dom.minidom.parseString( str( m.edit_config(ospf, target='running') ) )
print (xmlDom.toprettyxml( indent = "  " ))

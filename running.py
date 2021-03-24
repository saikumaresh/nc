from ncclient import manager

with manager.connect(host='10.10.20.48', port=830, username='cisco1', password='cisco1' , hostkey_verify=False) as m:
    c = m.get_config(source='running').data_xml
    with open('running_config.txt', 'w') as f:
        f.write(c)

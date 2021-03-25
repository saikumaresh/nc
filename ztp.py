 print "\n\n *** Sample ZTP Day0 Python Script *** \n\n"

 # Importing cli module
 import cli

 print "\n\n *** Executing show version *** \n\n"
 cli.executep('show version')

 print "\n\n *** Configuring a Loopback Interface *** \n\n"
 cli.configurep(["interface loop 100", "ip address 10.10.10.10 255.255.255.255", "end"])

 print "\n\n *** Executing show ip interface brief *** \n\n"
 cli.executep('show ip int brief')

 print "\n\n *** ZTP Day0 Python Script Execution Complete *** \n\n"

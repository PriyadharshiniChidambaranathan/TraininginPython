
import re  

url=input(" ")
print("URL:",url)
# finding the hostname which may
hostname = re.findall('://www.([\w\-\.]+)',url)
hostnameres = str(hostname)[1:-1]
print("Hostname:",hostnameres)

# finding the protocol 
protocol = re.findall('(\w+)://',url)
protocolres = str(protocol)[1:-1]
print("Protocol:",protocolres)

#finding the portnumber
portnum = re.findall('.com:(\d+)?', url)
portnumres = str(portnum)[1:-1]
print("Port number:",portnumres)


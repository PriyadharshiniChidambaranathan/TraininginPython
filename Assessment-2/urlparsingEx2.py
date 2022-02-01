
import re  


url=input(" ")
  
# finding the protocol 
protocol = re.findall('(\w+)://',url)
print("Protocol:",protocol)
  
# finding the hostname which may
hostname = re.findall('://www.([\w\-\.]+)', url)
print("Hostname:",hostname)

#finding portnum
portnum = re.findall('(:(\d+))?',url)
print("Port Number:",portnum)

import re

def ValidateURL(str):

	# Regex to check valid URL
	regex = ("((http|https)://)(www.)" +"[a-zA-Z0-9@:%._\\+~#?&//=]" +"{2,256}\\.[a-z]" +"{2,6}\\b([-a-zA-Z0-9@:%" +"._\\+~#?&//=]*)")
	
	# Compile the ReGex
	URL = re.compile(regex)

	if (str == None):
		return False
	if(re.search(URL, str)):
		return True
	else:
		return False

url =input(" ")
if(ValidateURL(url) == True):
	print("Yes")
else:
	print("No")


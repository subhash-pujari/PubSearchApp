import urllib

'''
 this is the client to get the data from lucene search apis
'''

class httpClient:
	
	def __init__(self):
		self.url = "www.google.com"

	def request(self, url):
		return urllib.urlretrieve(url)

class xmlParser:
	def __init__(self):
		print "parser init"

	def parse(self, xml):
		print xml

def main():


	testData = "<result><pub>\n<id>\n1712314\n</id>\n<title>\nstatistical mechanics\n</title>\n</pub>\n<pub>\n<id>\n1234\n</id>\n<title>\nabcd\n</title>\n</pub>\n</result>"

	parser = xmlParser()
	parser.parse(testData)
	client = httpClient()
	for line in client.request("http://www.google.com"):
		print line

if __name__ == "__main__":
	main()




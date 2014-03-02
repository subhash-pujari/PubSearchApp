import database


dataDir = "../../PubDataSet/"

commDataset = "nodeDegAllNetData.csv"
commFile = "nodeComm.tsv"
citNw = "citNw.tsv"
pubCoauth = "pubCoauth.tsv"


def main():

	db = database.DatabaseHandler()

	# store comm id
	'''
	fileR = open(dataDir+commDataset)
	fileW = open(dataDir + commFile, "w" )
	
	for line in fileR:

		if line.find("Class") > 0:
			continue

		line = line.replace("\n", "")

		tokens = line.split(" ")

		comm = tokens[2]
		_id = tokens[1]
		
		if db.getTitle(_id) is None:
			continue

		fileW.write(_id + "\t" + comm + "\t" + db.getTitle(_id)+ "\n")
				
	# store cit nw

	# store pubCoauth
	fileR = open(dataDir + commFile)
	fileW = open(dataDir+pubCoauth, "w")
	for line in fileR:
		print line
		line = line.replace("\n", "")
		
		tokens = line.split("\t")
		_id = tokens[0]

		authList = db.getAuthList(_id)
	
		wLine = _id
		if authList is None:
			continue
		for auth in authList:
			wLine = wLine + "\t" + str(auth)

		wLine = wLine + "\n"
		print wLine
		fileW.write(wLine)
	'''
	
	# store citation nw
	fileR = open(dataDir + commFile)
	fileW = open(dataDir + citNw, "w")
	count = 0

	for line in fileR:
		#print line
		count = count + 1
		print "count>>" + str(count)
		line = line.replace("\n", "")
		
		tokens = line.split("\t")
		pub = tokens[0]
		
		neighSet = db.getNeigh(pub)

		for neigh in neighSet:
			fileW.write(pub + "\t" +str(neigh) + "\n")
	
	#db.getTitle()
	print "hello"

if __name__ == "__main__":
	main()

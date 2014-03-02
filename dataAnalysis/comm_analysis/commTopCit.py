'''
 This script is to get the top citation publication in a community.
'''

import database
from operator import itemgetter

dataDir = "../../PubDataSet/"
commFile = "nodeComm.tsv"



def main():
	
	db = database.DatabaseHandler()

	# create a dict of comm with pub and cit count 
	print "hello"
	commDict = dict()

	fileR = open(dataDir + commFile)

	for line in fileR:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		_id = tokens[0]
		comm = tokens[1]

		if comm not in commDict:
			commDict[comm] = list()

		else:
			citCount = db.getCitCount(_id)
			title = db.getTitle(_id)

			if title is None or citCount is None:
				continue

			commDict[comm].append((title, citCount))

	fileW = open(dataDir + "topPub.tsv", "w")

	for comm in commDict:
		
		pubList = commDict[comm]
		pubList = sorted(pubList,key=itemgetter(1))
		if len(pubList) > 10:
			for i in range(10):
				item = pubList[(i+1)*-1]
				print comm +">>"+str(item)
				fileW.write(comm+"\t"+str(item[0])+">>"+str(item[1]) + "\n")	

if __name__ == "__main__":
	main()

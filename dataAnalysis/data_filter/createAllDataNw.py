'''
	This script is tpo create a data network of all the publication we have the data for.
'''

import database

dataDir = "../../PubDataSet/"
commFile = "nodeComm.tsv"

def main():
	
	db = database.DatabaseHandler()

	fileR = open(dataDir + commFile)
	pubSet = set()

	for line in fileR:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		pubSet.add(tokens[0])
		
	print "len pubSet>>" + str(len(pubSet))
	
	fileW = open("coauth_notPrime.tsv", "w")

	pubCitList = list()
	
	for i in range(130):

		#fileW = open("coauth_notPrime"+str(i+1)+".tsv", "w")

		lowerBound = i * 100000 + 1
		upperBound = (i+1) * 100000
		pubCitList = db.getCitRef(lowerBound, upperBound);
		for item in pubCitList:
			if item[0] in pubSet or item[1] in pubSet:
				fileW.write(item[0]+ "\t" +item[1] + "\n")	

if __name__ == "__main__":
	main()

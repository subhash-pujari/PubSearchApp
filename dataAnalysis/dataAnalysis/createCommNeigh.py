'''
This script stores the information about the communities which have more than 10 publications and thus filter the number of publication.

'''


dataDir = "/home/pujari/dataAnalysis/"
file = "nodeComm.tsv"
coAuth = "coauth_notPrime.tsv"
def main():

	# this file have pub comm data
	fileR = open(dataDir + file)
	
	# to find number of publication in each community
	commDict = dict()
	
	# to store a map from pub to comm
	valPubDict = dict()

	# contain name of the comm having # pub > 10
	valCommList = list()

	# store pub-comm and comm-pubSet
	for line in fileR:
		line  = line.replace("\n", "")

		tokens = line.split("\t")

		_id = tokens[0]
		comm = tokens[1]

		valPubDict[_id] = comm

		if comm in commDict:
			# if the comm is already present store the data
			commDict[comm].add(_id)
		else:
			# else create a new set and store the data
			commDict[comm] = set()
			commDict[comm].add(_id)
	
	# check the number of publication in a community and take only the communities with publication more than 10 and store them in the valVommList.
	for comm in commDict:

		commSet = commDict[comm]

		# if len(commSet) > 10 then store in valCommList
		if len(commSet) > 10:
			valCommList.append(comm)


	# this is the main dict that stores following mapping comm - pub - neighSet
	commPubDict = dict()

	#for each comm in valCommList init the dict with its first mapping
	for comm in valCommList:
		commPubDict[comm] = dict()
	
	#read the citation data
	fileR = open(dataDir + coAuth)


	# for each line in which comm is the node and then put that node as in that comm and initialise the neigh set
	for line in fileR:
		line = line.replace("\n", "")

		tokens = line.split("\t")

		pub1 = tokens[0]
		pub2 = tokens[1]
		
		if pub1 in valPubDict:
			comm = valPubDict[pub1]
			
			if comm not in commPubDict:
				continue

			pubDict = commPubDict[comm]
			if pub1 in pubDict:
				commPubDict[comm][pub1].add(pub2)
			else:
				commPubDict[comm][pub1] = set()
				commPubDict[comm][pub1].add(pub2)

		if pub2 in valPubDict:
			comm = valPubDict[pub2]

			if comm not in commPubDict:
				continue

			pubDict = commPubDict[comm]
			if pub2 in pubDict:
				commPubDict[comm][pub2].add(pub1)									
			else:
				commPubDict[comm][pub2] = set() 
				commPubDict[comm][pub2].add(pub1)


	for comm in commPubDict:
		fileW = open(dataDir + "coAuthcomm" + comm + ".tsv", "w")
		
		pubDict = commPubDict[comm]
		
		for pub in pubDict:
			pubSet = pubDict[pub]

			for neigh in pubSet:
				fileW.write(pub + "\t" + neigh + "\n")

		fileW.close()	

	print "hello"


if __name__ == "__main__":
	main()

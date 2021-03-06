'''
	this script find the k means within a community and number of k is taken as 1% of the publication in the community.
'''	

import random
from operator import itemgetter
from os import listdir
from os.path import isfile, join

dataDir = "/home/pujari/dataAnalysis/"


class kMean:

	def __init__(self, pubNeighDict):
		
		# make object of the simillarity class
		self.sim = SimMeasure()

		# create neigh dict
		self.neighDict = pubNeighDict
		
		# publication in the community
		self.pubs = self.neighDict.keys()

		#cluster points
		self.clustPoints = list()

		# get the random ids
		randIds = self.choseKRand(self.neighDict.keys())
		
		# find the random points using the random ids
		for _id in randIds:
			self.clustPoints.append(self.pubs[_id])

		print "len>>" + str(len(self.clustPoints))

		# cluster dict which contains the cluster and items in that cluster
		#self.clustDict = dict()
		

	def choseKRand(self, itemList):

		k = int(.01 * len(itemList))
		print str(len(itemList))
		list = [range(len(itemList))]
		#print list
		randIds = random.sample(list[0], k)	
		print "len(randIds)>>" + str(len(randIds))
		return randIds

	def clust(self):


		clustDict = dict()

		for index in range(10):
			
			# check the nearest cluster of the publication 
			for pub in self.pubs:
				simList = list()
				for i in range(len(self.clustPoints)):
					simScore = self.sim.jaccardSim(self.neighDict[self.clustPoints[i]], self.neighDict[pub])
					simList.append((i, simScore))

					
				# sort on basis of sim score
				simList = sorted(simList,key=itemgetter(1))

				if len(simList) == 0:
					continue
				#take the one with highest sim score in case of conflict take random
				_tuple = simList[-1]

				# this is the cluster to which the pub is closest
				cluster = _tuple[0]

				# store pub in clustDict
				if cluster in clustDict:
					clustDict[cluster].append(pub)
				else:
					clustDict[cluster] = list()
					clustDict[cluster].append(self.clustPoints[int(cluster)])
					clustDict[cluster].append(pub)



			# find new centroid in each cluster
			for clust in clustDict:
				pubList = clustDict[clust]

				pubDict = dict()

				for pub1 in pubList:
					pubDict[pub1] = list()

					for pub2 in pubList:
						if pub1 == pub2:
							continue

						pubDict[pub1].append((pub2, self.sim.jaccardSim(self.neighDict[pub1], self.neighDict[pub2])))
					
				pubSimSumList = list()
				for pub in pubDict:
					
					total = sum([pair[1] for pair in pubDict[pub]])
					pubSimSumList.append((pub, total))


				pubSimSumList = sorted(pubSimSumList, key=itemgetter(1))

				_tuple = pubSimSumList[-1]
				
				print index
				print clust
				print "tuple>>" + str(_tuple)
				print str(pubSimSumList[-2])

			# update the custPoints for respective clusters with the new id
				self.clustPoints[clust] = _tuple[0]


		return clustDict
class SimMeasure:

	def __init__(self):
		print "init Sim Measure"

	def jaccardSim(self, set1, set2):
		simScore = float(len(set1.intersection(set2)))/float(len(set1.union(set2)))
		return simScore


def createNeighDict(filename):
	
	fileR = open(filename)

	# the neigh dict having pub - neighSet
	neighDict =  dict()

	for line in fileR:
		line = line.replace("\n", "")

		tokens = line.split("\t")

		pub = tokens[0]

		neigh = tokens[1]

		if pub in neighDict:
			neighDict[pub].add(neigh)
		else:
			neighDict[pub] = set()
			neighDict[pub].add(neigh)

	return neighDict

def saveToFile(fileName, dict):

	fileW = open(fileName, "w")

	for clust in dict:
		for pub in dict[clust]:
			fileW.write(str(clust) + "\t" + str(pub) + "\n")


		
def main():
	print "hello"

	path = "../commFiles/"

	# get filenames of all comm
	allfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
	print allfiles

	for fileName in allfiles:
		if fileName.find('Authcomm') < 0:
			continue
		else:
			comm = fileName[fileName.find('coAuthcomm')+10 : fileName.find('.')]

			#filename = "../commFiles/coAuthcomm166.tsv"
			neighDict = createNeighDict(path+fileName)
			clustAlgo = kMean(neighDict)
			clustDict = clustAlgo.clust()
			saveToFile("commClust"+comm+".tsv", clustDict)


if __name__ == "__main__":
	main()

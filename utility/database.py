'''
database interface
'''

import MySQLdb

class DatabaseHandler:
	
	def __init__(self):
		self.db = MySQLdb.connect('localhost', 'username', 'password', 'database_name')
		self.cursor = self.db.cursor()

	def getTitle(self, _id):
		sql = "select Title from Publication where ID = "+_id +";"
		self.cursor.execute(sql)
		data = self.cursor.fetchone()

		if data is None:
			return

		return data[0]

	def getCitCount(self, _id):
		sql = "select CitationCount from Publication where ID= " + _id + ";"

		self.cursor.execute(sql)
		data = self.cursor.fetchone()
		if data is None:
			return
		return data[0]

	def getAuthList(self, pub):
		sql = "select Author1, Author2, Author3, Author4, Author5, Author6, Author7 from Publication where ID = "+ pub +";"
		self.cursor.execute(sql)
		data = self.cursor.fetchone()
		authList = list()

		print pub
		print data

		if data is None:
			return

		for i in range(7):
			
			auth = data[i]
			if auth is None:
				continue

			else:
				authList.append(auth)	
				
		return authList

	def getCit(self, pub):
	
		citSet = set()

		sql = "select PublicationID from PublicationReferenceCitation where type = 1 and citationreference = "+ pub +";"

		self.cursor.execute(sql)
		data = self.cursor.fetchall()

		for line in data:
			#print line
			citSet.add(str(line[0]))

		print "citSet1>>" + str(len(citSet))

		sql = "select citationreference from PublicationReferenceCitation where type = 0 and PublicationID = "+ pub +";"

		self.cursor.execute(sql)
		data = self.cursor.fetchall()

		for line in data:
			#print line
			citSet.add(str(line[0]))

		print "citSet2>>" + str(len(citSet))


		return citSet

	def getRef(self, pub):

		refSet = set()
		
		sql = "select citationreference from PublicationReferenceCitation where type = 1 and PublicationID = "+ pub + ";"

		self.cursor.execute(sql)

		data = self.cursor.fetchall()
		print data
		for line in data:
			#print line
			refSet.add(line[0])

		print str(len(refSet))

		return refSet


	def getNeigh(self, pub):

		totalSet = set()

		totalSet = totalSet.union(self.getCit(pub))
		print "totalSet cit>>" + str(len(totalSet))

		totalSet = totalSet.union(self.getRef(pub))
		print "total Set ref>>" + str(len(totalSet))

		return totalSet

	def getCitRef(self, lower, upper):
	
		sql = "select * from PublicationReferenceCitation where id >= "+ str(lower) + " and id <= "+ str(upper) + ";"
		print sql
		self.cursor.execute(sql)
		data = self.cursor.fetchall()

		#print data


		citRefList = list()

		for tokens in data:
			_id = tokens[0]
			pub = tokens[1]
			citRef = tokens[2]
			_type = tokens[3]
			citRefList.append((str(pub), str(citRef)))				
		return citRefList

def main():
	db = DatabaseHandler()
	print db.getTitle("1712314")
	print db.getAuthList("1712314")
	db.getNeigh("1712314")
	print str(len(db.getCitRef(1, 1000000)))

if __name__ == "__main__":
	main()

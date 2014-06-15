import logging
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoClinq:
	def __init__(self):
		logging.debug("Init MongoClinq Database")

	def AppStartUp(self,app,args):
		
		logging.debug("Creating Mogno Client")

		try:
			logging.info("Connecting to Mongod: %s",app.config.dbPath)
			self.client = MongoClient(app.config.dbPath)

			self.cls = {}
			self.SetupCollections(app)

		except Exception, e:
			logging.error("%s", e)
			logging.error("Unable to connect to database %s", e)

		app.dataLayer = self

	def SetupCollections(self,app):
		#setup main collection
		logging.debug("Creating main collection in mongodb")

		self.db = self.client[app.config.dbname] 

		self.cls["fs"] = self.db["clinqFiles"]

	def StoreFileById(self,docId, document):
		document["docid"] = docId

		logging.debug("Storing object %s", document)

		udRes = self.cls["fs"].update({"docid": document["docid"]}, document)

		logging.debug("Update db result: %s",udRes)

		if not udRes["updatedExisting"]:
			self.cls["fs"].insert(document)


	def GetFileById(self, docId):

		queryObj = {"docid": docId}

		logging.debug("Searching in db for: %s", queryObj)

		return self.cls["fs"].find_one(queryObj)

	def GetChildsById(self, id):

		searchObj = {"parent": id}

		logging.debug("Searching in db for: %s", searchObj)

		result = list(self.cls["fs"].find(searchObj))

		logging.debug("Found %s Items", len(result))

		return result
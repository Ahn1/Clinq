import logging
from pymongo import MongoClient

class MongoClinq:
	def __init__(self):
		logging.debug("Init MongoClinq Database")

	def AppStartUp(self,app,args):
		
		logging.debug("Creating Mogno Client")

		try:
			self.client = MongoClient(app.config.dbPath)

			self.cls = {}
			self.SetupCollections()

		except Exception, e:
			logging.error("%s", e)
			logging.error("Unable to connect to database %s", moduledir)

	def SetupCollections(self):
		#setup main collection
		main = self.cls["clinq"] = self.client["clinq_files"]
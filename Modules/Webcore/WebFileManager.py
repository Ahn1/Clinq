import logging
import os

class WebFileManager:
	def __init__(self,app):
		self.app = app
		self.dir = os.path.join(self.config.tmpDir, "webserver")

		if not os.path.exists(self.dir):
				logging.info("Creating web dir '%s'", self.dir)
				os.makedirs(self.dir)




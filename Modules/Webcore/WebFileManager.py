import logging
import os
import shutil

class WebFileManager:
	def __init__(self,app):

		

		self.app = app
		self.dir = os.path.join(app.config.tmpDir, "webserver")
		self.staticdir = os.path.join(app.config.tmpDir, "webserver-static")

		logging.debug("Create Web File manager on '%s'", self.dir)

		try:
			shutil.rmtree(self.dir)
			shutil.rmtree(self.staticdir)
		except Exception, e:
			pass
		

		if not os.path.exists(self.dir):
				logging.info("Creating web dir '%s'", self.dir)
				os.makedirs(self.dir)

		if not os.path.exists(self.staticdir):
				logging.info("Creating web static dir '%s'", self.staticdir)
				os.makedirs(self.staticdir)

	def AddFolder(self, targetPath ,sourcePath):
		joinedTarget = os.path.join(self.dir, targetPath)

		logging.debug("Try to copy '%s' to '%s'", sourcePath, joinedTarget)

		shutil.copytree(sourcePath, joinedTarget)

	def AddFile(self,targetPath ,sourcePath):
		
		joinedTarget = os.path.join(self.dir, targetPath)

		logging.debug("Try to copy '%s' to '%s'", sourcePath, joinedTarget)

		shutil.copy(sourcePath, joinedTarget)


	def AddFolderStatic(self, targetPath ,sourcePath):
		joinedTarget = os.path.join(self.staticdir, targetPath)

		logging.debug("Try to copy '%s' to '%s'", sourcePath, joinedTarget)

		shutil.copytree(sourcePath, joinedTarget)

	def GetPath(self, targetPath):
		return os.path.join(self.dir, targetPath)

	def GetStaticPath(self, targetPath):
		return os.path.join(self.staticdir, targetPath)

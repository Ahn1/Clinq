import logging
import hashlib
import os


def Info():
	return {
		"name": "Indexing",
		"version": "0.1"
	}

def Register(app):
	app.RegisterAppCommand("StartCompleteIndexing",StartCompleteIndexing)

	app.RegisterCommand("indexing",StartCompleteIndexing)



def StartCompleteIndexing(app,args):
	logging.info("Start complete index refresh for %s", app.config.datadir)

	app.appcommands["EnsureFolder"](app.config.datadir)
	app.appcommands["EnsureFolder"](app.config.IndexDir)

	RefreshFolderIndex(app,app.config.datadir)

	logging.info("Index refresh completed")


def RefreshFolderIndex(app,path):

	logging.debug("Start indexing %s",path)

	oslist = os.listdir(path)
	oslist = [os.path.join(path,f) for f in oslist]

	files = [f for f in oslist if os.path.isfile(f)]
	dirs = [f for f in oslist if os.path.isdir(f)]

	for subdir in dirs:
		RefreshFolderIndex(app,subdir)

	for targetFile in files:
		RefreshFileIndex(app,targetFile)

	childs = app.dataLayer.GetChildsById(hashlib.md5(path).hexdigest())

	logging.debug("Total length of '%s' is %s Seconds",path, GetCompleteDuration(childs))

	
def GetCompleteDuration(childs):
	sumDur = 0.0

	for child in childs:
		if "length" in child:
			sumDur += child["length"]

	return sumDur
		

def RefreshFileIndex(app,targetFile):
	logging.debug("Handling file %s", targetFile)

	fileName, fileExtension = os.path.splitext(targetFile)

	fileTag = {}

	handler = app.GetTagHandler(fileExtension)

	parent = os.path.dirname(targetFile)
	fileTag["parent"] = hashlib.md5(parent).hexdigest()

	if handler is not None:
		handler(targetFile,fileTag)

		fileTag["isFile"] = True

		app.dataLayer.StoreFileById(hashlib.md5(targetFile).hexdigest(), fileTag)

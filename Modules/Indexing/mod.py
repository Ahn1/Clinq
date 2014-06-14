import logging
import hashlib
import os

from Lib import FileHash


def Info():
	return {
		"name": "indexing",
		"version": "0.3",
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


	dirTag = {}

	childs = app.dataLayer.GetChildsById(FileHash.GetPathHash(app,path))
	dirTag["length"] = GetCompleteDuration(childs)

	parent = os.path.dirname(path)

	if path != app.config.datadir:
		dirTag["parent"] = FileHash.GetPathHash(app,parent)

	#Set title to Folder name
	dirTag["title"] = os.path.relpath(path,parent)

	# Set path
	dirTag["path"] = FileHash.GetRelPath(app,path)

	app.dataLayer.StoreFileById(FileHash.GetPathHash(app,path), dirTag)
		


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
	fileTag["parent"] = FileHash.GetPathHash(app,parent)

	fileTag["isFile"] = True

	# Set path
	fileTag["path"] = FileHash.GetRelPath(app,targetFile)

	if handler is not None:
		handler["UpdateTag"](app,targetFile,fileTag)

		app.dataLayer.StoreFileById(FileHash.GetPathHash(app,targetFile), fileTag)
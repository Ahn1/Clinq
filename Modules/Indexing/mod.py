import logging
import hashlib
import os

from Lib import FileHash


def Info():
	return {
		"name": "indexing",
		"version": "1.0",
	}

def Register(app):
	app.RegisterAppCommand("StartCompleteIndexing",StartCompleteIndexing)

	app.RegisterCommand("indexing",StartCompleteIndexing)



def StartCompleteIndexing(app,args):
	logging.info("Start complete index refresh for %s", app.config.datadir)

	app.appcommands["EnsureFolder"](app.config.datadir)

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
	dirTag["filesize"] = GetCompleteFileSize(childs)

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

def GetCompleteFileSize(childs):
	return sum([x["filesize"] for x in childs if "filesize" in x])
		

def RefreshFileIndex(app,targetFile):
	logging.debug("Handling file %s", targetFile)

	relTargetFile = FileHash.GetRelPath(app,targetFile)

	fileHash = FileHash.GetPathHash(app,relTargetFile)

	# Get file database, if exists
	storedDoc = app.dataLayer.GetFileById(fileHash)

	# get file system info for file
	fileInfo = os.stat(targetFile)

	logging.debug("Trying to get stored file: %s", storedDoc)

	# exit if file has not changed
	if storedDoc is not None:
		if "modified" in storedDoc:
			if storedDoc["modified"] == fileInfo.st_mtime:
				logging.debug("Skip file '%s', because it hasn't changed", relTargetFile)
				return

	# get file names
	fileName, fileExtension = os.path.splitext(relTargetFile)

	fileTag = {}

	fileTag["modified"] = fileInfo.st_mtime
	fileTag["filesize"] = fileInfo.st_size 

	# Get a handler for reading tags
	handler = app.GetTagHandler(fileExtension)

	parent = os.path.dirname(relTargetFile)
	fileTag["parent"] = FileHash.GetPathHash(app,parent)

	fileTag["isFile"] = True

	# Set path
	fileTag["path"] = relTargetFile

	# Updating document
	if handler is not None:
		handler["UpdateTag"](app,targetFile,fileTag)

	app.dataLayer.StoreFileById(fileHash, fileTag)
import logging
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
		logging.debug("Handling file %s", targetFile)

		fileName, fileExtension = os.path.splitext(targetFile)

		handler = app.GetTagHandler(fileExtension)
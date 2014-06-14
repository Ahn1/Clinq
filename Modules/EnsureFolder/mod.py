import logging
import os


def Info():
	return {
		"name": "Ensure Folder",
		"version": "0.1"
	}

def Register(app):
	app.RegisterAppCommand("EnsureFolder",EnsureFolder)
	app.RegisterAppCommand("EnsureLocalFolder",EnsureLocalFolder)


def EnsureLocalFolder(folder):
	EnsureFolder(os.path.join("./",folder))

def EnsureFolder(folder):
	logging.debug("Check if '%s' exists",folder)
	if not os.path.exists(folder):
		logging.debug("Create '%s' beacause it deos not exists", folder)
		os.makedirs(folder)

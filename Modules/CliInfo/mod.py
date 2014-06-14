import logging
import os

from Lib import FileHash


def Info():
	return {
		"name": "cli_media_info",
		"version": "0.2",
		"core": True
	}

def Register(app):
	app.RegisterCommand("info",RessourceInfo)


def RessourceInfo(app,args):
	args = args[2:]

	targeRessource = "./"

	if len(args) > 0:
		targeRessource = args[len(args) - 1]

	targeRessource = os.path.abspath(targeRessource)

	logging.info("Get info for '%s'", targeRessource)

	nodes = app.dataLayer.GetChildsById(FileHash.GetPathHash(app, targeRessource))

	nodes.append(GetFileInfo(app, targeRessource))

	pathLenght = max([len(x["path"]) for x in nodes if "path" in x])

	lengths = [ReadableNodeLength(x) for x in nodes]
	maxLengths = max([len(x) for x in lengths])

	for i,node in enumerate(nodes):
		out = ""

		path = node.get("path")

		if(path == ""):
			path = "."

		out += path.ljust(pathLenght + 2, " ")

		out += lengths[i].ljust(maxLengths," ")

		print(out)
		


def ReadableNodeLength(node):

	length = node.get("length")

	minutes = str(int(length / 60)).rjust(2,"0")
	second = str(int(length % 60)).rjust(2,"0")

	return "" + minutes + ":" + second

def GetFileInfo(app,path):
	return app.dataLayer.GetFileById(FileHash.GetPathHash(app,path))

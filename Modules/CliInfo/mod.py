import logging
import os

from Lib import FileHash


def Info():
	return {
		"name": "cli_media_info",
		"version": "0.3",
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

	nodes = [x for x in app.dataLayer.GetChildsById(FileHash.GetPathHash(app, targeRessource)) if x is not None]

	print nodes

	currentNode = GetFileInfo(app, targeRessource)
	if currentNode is not None:
		nodes.append(currentNode)

	pathLenght = max([len(x["path"]) for x in nodes if ("path" in x)])

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

		logging.debug("Printing info: %s", out)
		


def ReadableNodeLength(node):

	if "length" not in node:
		return ""

	length = node.get("length")

	minutes = int(length / 60)

	hours = int(minutes / 60)

	minutes = str(minutes - (hours * 60)).rjust(2,"0")

	hours = str(hours).rjust(2,"0")

	second = str(int(length % 60)).rjust(2,"0")
	
	res = "" + hours + ":" + minutes + ":" + second

	logging.debug("Get length: %s", res)

	return res

def GetFileInfo(app,path):
	return app.dataLayer.GetFileById(FileHash.GetPathHash(app,path))

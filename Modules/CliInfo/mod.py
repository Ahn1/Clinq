import logging
import os

from Lib import FileHash


def Info():
	return {
		"name": "cli_media_info",
		"version": "0.4",
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

	currentNode = GetFileInfo(app, targeRessource)
	if currentNode is not None:
		nodes.append(currentNode)

	pathLenght = max([len(x["path"]) for x in nodes if ("path" in x)])

	for node in nodes:
		node["ReadableNodeLength"] = ReadableNodeLength(node)
		node["ReadableFileSize"] = ReadableFileSize(node)

	maxReadableLengthLength = max([len(x["ReadableNodeLength"]) for x in nodes])
	maxFileSizeLength = max([len(x["ReadableFileSize"]) for x in nodes])

	nodes = sorted(nodes, key=lambda k: k['filesize'])

	for i,node in enumerate(nodes):
		out = ""

		path = node.get("path")

		if(path == ""):
			path = "."

		out += path.ljust(pathLenght + 2, " ")

		out += node["ReadableNodeLength"].rjust(maxReadableLengthLength + 2," ")

		out += node["ReadableFileSize"].rjust(maxFileSizeLength + 2," ")

		print(out)

		#logging.debug("Printing info: %s", out)
		

def ReadableFileSize(node):
	if "filesize" not in node:
		return ""

	currentSize = float(node["filesize"])

	prefixes = ['','k','m','g','t']
	pot = 0

	while currentSize > 1024:
		pot += 1
		currentSize = currentSize / 1024

	return str(int(currentSize)) + " " + prefixes[pot] + "B"



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


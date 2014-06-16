import logging
from flask import Flask
from Lib.event import Event

from Modules.Webcore.WebFileManager import WebFileManager

def Info():
	return {
		"name": "web-core",
		"version": "0.1",
		"core": False
	}

def Register(app):
	app.SetAppComponent("WebFileManager", WebFileManager(app))

	# Create a new event in app compnent, that raises, if the server starts
	app.SetAppComponent("WebcodeStartet",Event())


	templateFolder = app.GetAppComponent("WebFileManager").GetPath("")

	logging.debug("Init flask with template folder '%s'", templateFolder)

	flask = Flask(__name__,template_folder=templateFolder)
	
	@flask.route("/corestatus")
	def hello():
		return "Running"


	app.SetAppComponent("server", flask)

	app.RegisterCommand("server", RunServer)


def RunServer(app,args):

	logging.debug("Raise Webcode Started event")

	app.GetAppComponent("WebcodeStartet")(app,None)

	logging.info("Start running server")
	
	server = app.GetAppComponent("server")

	server.run()

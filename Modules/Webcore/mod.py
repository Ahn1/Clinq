import logging
from flask import Flask
from Lib.event import Event

from Modules.Webcore.WebFileManager import WebFileManager

def Info():
	return {
		"name": "web-core",
		"version": "0.1",
		"description": "Core for the webserver. Required by every web module",
		"core": False
	}

def Register(app):
	app.SetAppComponent("WebFileManager", WebFileManager(app))

	# Create a new event in app compnent, that raises, if the server starts
	app.SetAppComponent("WebcodeStartet",Event())


	templateFolder = app.GetAppComponent("WebFileManager").GetPath("")
	staticFolder = app.GetAppComponent("WebFileManager").GetStaticPath("")

	logging.debug("Init flask with template folder '%s' and static folder '%s'", templateFolder,staticFolder)

	flask = Flask(__name__,template_folder=templateFolder,static_url_path="/static",static_folder=staticFolder)
	
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

	server.run(host='0.0.0.0')

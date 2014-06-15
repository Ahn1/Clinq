import logging
from flask import Flask
from Lib.event import Event

def Info():
	return {
		"name": "web-core",
		"version": "0.1",
		"core": False
	}

def Register(app):
	flask = Flask(__name__)
	
	@flask.route("/corestatus")
	def hello():
		return "Running"

	app.SetAppComponent("server", flask)

	app.RegisterCommand("server", RunServer)

	# Create a new event in app compnent, that raises, if the server starts
	app.SetAppComponent("WebcodeStartet",Event())


def RunServer(app,args):

	logging.debug("Raise Webcode Started event")

	app.GetAppComponent("WebcodeStartet")(app,None)

	logging.info("Start running server")
	

	server = app.GetAppComponent("server")

	server.run()

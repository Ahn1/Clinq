import logging
from flask import Flask

def Info():
	return {
		"name": "web-core",
		"version": "0.1",
		"core": False
	}

def Register(app):
	flask = Flask(__name__)
	
	@flask.route("/clinq-web")
	def hello():
		return "Hello World!"

	app.SetAppComponent("server", flask)

	app.RegisterCommand("server", RunServer)


def RunServer(app,args):
	logging.info("Start running server")

	server = app.GetAppComponent("server")

	server.run()






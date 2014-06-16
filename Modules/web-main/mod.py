import logging
import os

from flask import Flask, render_template, make_response


def Info():
	return {
		"name": "web-main",
		"version": "0.1",
		"core": False
	}



def Register(app):


	# Register for server start event
	runServerEvent = app.GetAppComponent("WebcodeStartet")

	runServerEvent += ServerStarted




def ServerStarted(app, args):

	# Get directory of current module
	scriptDir = os.path.dirname(__file__)

	# Get directory of required template files
	webFile = os.path.join(scriptDir,"web/webmain")

	# Copy template files of mudole to the server
	app.GetAppComponent("WebFileManager").AddFolder("webmain",webFile)
	logging.info("Copied '%s' to webserver filemanager", webFile)

	flask = app.GetAppComponent("server")

	@flask.route("/")
	def index():
		return render_template("webmain/index.html")

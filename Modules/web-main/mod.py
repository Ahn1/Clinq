import logging
import os

from flask import Flask, render_template, make_response
from Lib.event import Event


def Info():
	return {
		"name": "web-main",
		"version": "0.2",
		"description": "Main module for webserver. Includes a startpage and the master page",
		"core": False
	}


webMainscripDir = ""

def Register(app):

	global webMainscripDir
	webMainscripDir = os.path.dirname(__file__)

	# Setup web events for other modules
	app.SetAppComponent("WebHeaderRequested", Event())

	app.RegisterAppCommand("GetWebTemplateParameter", GetWebTemplateParameter)

	# Register for server start event
	runServerEvent = app.GetAppComponent("WebcodeStartet")
	runServerEvent += ServerStarted


def GetWebTemplateParameter(app):
	logging.debug("Requested common web parameter")

	parameter = {}
	parameter["menuTemplates"] = []
	parameter["availible"] = "True"

	app.GetAppComponent("WebHeaderRequested")(app,parameter)

	logging.debug("Web parameters are: %s", parameter)

	return parameter

def ServerStarted(app, args):

	# Get directories of required  files
	webFolder = os.path.join(webMainscripDir,"web/webmain")
	staticsFolder = os.path.join(webMainscripDir,"web/static")

	# Copy template files of mudole to the server
	app.GetAppComponent("WebFileManager").AddFolder("webmain",webFolder)

	app.GetAppComponent("WebFileManager").AddFolderStatic("webmain",staticsFolder)

	app.GetAppComponent("WebFileManager").AddFile("",os.path.join(webMainscripDir,"web/template.html"))




	flask = app.GetAppComponent("server")

	@flask.route("/")
	def ShowStartPage():
		return render_template("webmain/index.html",webparam=app.appcommands["GetWebTemplateParameter"](app))

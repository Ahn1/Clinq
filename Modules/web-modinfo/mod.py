import logging
import os

from flask import Flask, render_template, make_response


def Info():
	return {
		"name": "web-modinfo",
		"version": "0.3",
		"description": "Show a page on website which displays all active modules",
		"core": False
	}

def Register(app):
	

	logging.debug("Set script dir for web-modinfo to '%s'", webModinfoScriptDir)


	app.OnStartup += OnAppStartup

	

def OnAppStartup(app, parameter):
	# Register event for web header
	requestEvent = app.GetAppComponent("WebHeaderRequested")
	requestEvent += GetmMenuTemplate

	# Register for server start event
	serverStartEvent = app.GetAppComponent("WebcodeStartet")
	serverStartEvent += RegisterModInfo



def GetmMenuTemplate(app,parameter):
	parameter["menuTemplates"].append("<a href='/modinfo' class='element'>Modinfo</a>")


def RegisterModInfo(app, args):

	webModinfoScriptDir = os.path.abspath(os.path.dirname(__file__))

	# Get directories of required  files
	webFolder = os.path.join(webModinfoScriptDir,"web/templates")
	staticsFolder = os.path.join(webModinfoScriptDir,"web/static")

	# Copy template files of mudole to the server
	app.GetAppComponent("WebFileManager").AddFolder("modinfo",webFolder)

	app.GetAppComponent("WebFileManager").AddFolderStatic("modinfo",staticsFolder)

	flask = app.GetAppComponent("server")

	@flask.route("/modinfo")
	def ShowModInfoPage():

		modulInfos = app.appcommands["GetActiveModules"]()
		modulInfos = sorted(modulInfos, key=lambda k: k['name'])


		return render_template("modinfo/modinfo.html",webparam=app.appcommands["GetWebTemplateParameter"](app), modInfos=modulInfos)

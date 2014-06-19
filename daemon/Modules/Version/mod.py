import logging

def Info():
	return {
		"name": "version",
		"version": "0.2",
		"description": "'version' command for cli",
		"core": True
	}

def Register(app):
	app.RegisterCommand("version",Run)
	
def Run(app,params):
	info = {
		"AppName": "Clinq",
		"Version": "0.2"
	}


	print(info["AppName"] + " " + info["Version"])
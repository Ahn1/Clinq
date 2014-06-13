import logging

def Info():
	return {
		"name": "version",
		"version": "0.1"
	}

def Register(app):
	app.RegisterCommand("version",Run)
	
def Run(app,params):
	info = {
		"AppName": "Clinq",
		"Version": "0.1"
	}


	print(info["AppName"] + " " + info["Version"])
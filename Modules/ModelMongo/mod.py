import logging
import sys

from Modules.ModelMongo.MongoClinq import MongoClinq


def Info():
	return {
		"name": "Mongo DB Backend",
		"version": "0.1"
	}

def Register(app):

	db = MongoClinq()

	app.OnStartup += db.AppStartUp

import logging
import sys

from Modules.ModelMongo.MongoClinq import MongoClinq


def Info():
	return {
		"name": "backend_mongo",
		"version": "0.1"
	}

def Register(app):

	db = MongoClinq()

	app.OnStartup += db.AppStartUp

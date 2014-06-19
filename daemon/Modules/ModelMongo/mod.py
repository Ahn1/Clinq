import logging
import sys

from Modules.ModelMongo.MongoClinq import MongoClinq


def Info():
	return {
		"name": "backend_mongo",
		"version": "0.4",
		"description": "Backend for mongoDB",
	}

def Register(app):

	db = MongoClinq()

	app.OnStartup += db.AppStartUp

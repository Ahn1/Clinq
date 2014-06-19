import imp
import inspect, os
import logging

import __main__ as main

activeModules = []

def LoadModules(mod,app):

	scriptDir = os.path.dirname(os.path.realpath(main.__file__))

	logging.debug("SCRIPT DIR: %s", scriptDir)

	top = os.path.join(scriptDir,"Modules")

	logging.info("Starting to import modules")

	for folder in os.listdir(top):

		if folder.startswith("__init__"):
			continue

		moduledir = os.path.join(top,folder)
		logging.info("Importing module %s",moduledir)

		try:
			moduleMain = os.path.join(moduledir,"mod.py")

			logging.debug("Importing main file %s", moduleMain)

			moduleCode = load_from_file(moduleMain)

			modInfo = moduleCode.Info()

			if ("core" in modInfo and modInfo["core"] == True) or (modInfo["name"] in app.config.modules):

				logging.debug("Register module '%s %s'", modInfo["name"], modInfo["version"])

				moduleCode.Register(app)

				activeModules.append(modInfo)

			else:
				logging.debug("Skip module %s", modInfo["name"])

		except Exception, e:
			logging.error("%s", e)
			logging.error("Cannot load module %s", moduledir)


	app.RegisterAppCommand("GetActiveModules",GetActiveModules)

def GetActiveModules():
	return activeModules


def load_from_file(filepath):
	class_inst = None
	xpected_class = 'MyClass'

	mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])

	if file_ext.lower() == '.py':
		py_mod = imp.load_source(mod_name, filepath)

	elif file_ext.lower() == '.pyc':
		py_mod = imp.load_compiled(mod_name, filepath)

	return py_mod
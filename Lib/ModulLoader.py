import imp
import os
import logging


def LoadModules(mod,app):
	top = "./Modules"

	logging.info("Starting to import modules")

	for folder in os.listdir(top):
		moduledir = os.path.join(top,folder)
		logging.info("Importing module %s",moduledir)

		try:
			moduleMain = os.path.join(moduledir,"mod.py")

			logging.debug("Importing main file %s", moduleMain)

			moduleCode = load_from_file(moduleMain)

			modInfo = moduleCode.Info()

			logging.debug("Importing module '%s %s'", modInfo["name"], modInfo["version"])

			moduleCode.Register(app)

		except Exception, e:
			logging.error("%s", e)
			logging.error("Cannot load module %s", moduledir)

def load_from_file(filepath):
	class_inst = None
	xpected_class = 'MyClass'

	mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])

	if file_ext.lower() == '.py':
		py_mod = imp.load_source(mod_name, filepath)

	elif file_ext.lower() == '.pyc':
		py_mod = imp.load_compiled(mod_name, filepath)

	return py_mod
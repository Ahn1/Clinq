import logging
import sys
import imp
from event import Event

class ClinqApp:
	def __init__(self):
		logging.debug("Init ClinqApp")

		self.commands = {}
		self.appcommands = {}
		self.tagHandler = {}

		self.dataLayer = None

		self.OnStartup = Event()

		try:
			logging.info("Load config file")
			self.config = imp.load_source("config", "./config.py")
		except:
			logging.error("Cannot load config file")
			

	def RegisterCommand(self,cmd,func):
		logging.debug("Registered command: %s", cmd)
		self.commands[cmd] = func

	def RegisterAppCommand(self,cmd,func):
		logging.debug("Register App Command: %s",cmd)
		if cmd not in self.appcommands:
			self.appcommands[cmd] = func
		else:
			logging.error("The app command '%s' already exists",cmd)

	def RegisterTagHandler(self,extension,func):
		logging.debug("Register Tag Handler")

		self.tagHandler[extension.lower()] = func

	def GetTagHandler(self,extension):
		extension = extension.lower()

		if extension in self.tagHandler:
			return self.tagHandler[extension]
		else:
			logging.debug("Cannot get Handler for '%s'", extension)
			return None



	def run(self):
		logging.info("Start runing app")
		
		logging.debug("Raise Startup event")
		self.OnStartup(self)

		args = sys.argv


		if len(args) > 1:
			if args[1] in self.commands:
				logging.debug("Execute command '%s'", args[1])
				self.commands[args[1]](self,args)
			else:
				logging.error("Command not found: %s", args[1])
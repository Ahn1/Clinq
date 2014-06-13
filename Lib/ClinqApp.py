import logging
import sys
import imp
from event import Event

class ClinqApp:
	def __init__(self):
		logging.debug("Init ClinqApp")

		self.commands = {}
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

	def run(self):
		logging.info("Start runing app")
		
		logging.debug("Raise Startup event")
		self.OnStartup(self)

		args = sys.argv

		if len(args) > 1:

			if args[1] in self.commands:
				self.commands[args[1]](self,args)
			else:
				logging.error("Command not found: %s", args[1])

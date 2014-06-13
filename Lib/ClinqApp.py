import logging
import sys

class ClinqApp:
	def __init__(self):
		logging.debug("Init ClinqApp")

		self.commands = {}
		self.dataLayer = None

	def RegisterCommand(self,cmd,func):
		logging.debug("Registered command: %s", cmd)
		self.commands[cmd] = func

	def run(self):
		logging.info("Start runing app")
		
		args = sys.argv

		if len(args) > 1:

			if args[1] in self.commands:
				self.commands[args[1]](self,args)
			else:
				logging.error("Command not found: %s", args[1])

#!/usr/bin/env python

import os
import __main__ as main
import Lib.ModulLoader as mod
from Lib.ClinqApp import ClinqApp

import logging

scriptDir = os.path.dirname(os.path.realpath(main.__file__))

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=os.path.join(scriptDir ,'clinq.log'),
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is mpler for console use
formatter = logging.Formatter('%(levelname)s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
#logging.getLogger('').addHandler(console)



def main():

	app = ClinqApp()

	modules = {}

	mod.LoadModules(modules,app)

	app.run()

if __name__ == '__main__':
	main()

import os
import clinq.models as model

from optparse import make_option
from django.core.management.base import BaseCommand, CommandError

from django.conf import settings

import clinq.management.commands.tagHandler as handler

class Command(BaseCommand):
	#option_list = BaseCommand.option_list + (
	#	make_option('--long', '-l', dest='long',
	#		help='Help for the long options'),
	#)
	help = 'Refresh media index'

	def handle(self, **options):
		path = settings.MEDIA_PATH
		print path

		self.IndexFolder(path)



	def IndexFolder(self, path):
		oslist = os.listdir(path)
		oslist = [os.path.join(path,f) for f in oslist]

		files = [f for f in oslist if os.path.isfile(f)]
		dirs = [f for f in oslist if os.path.isdir(f)]

		for subdir in dirs:
			self.IndexFolder(subdir)
			#print subdir

		for targetFile in files:
			self.IndexFile(targetFile)


	def IndexFile(self, path):
		fileName, fileExtension = os.path.splitext(path)

		relPath = os.path.relpath(path,settings.MEDIA_PATH)


		dbObj = None
		if model.File.objects.filter(path=relPath).count() == 0:
			dbObj = model.File()
			dbObj.path = relPath
		else:
			dbObj = model.File.objects.filter(path=relPath)[:1][0]

		lastEditTime = os.stat(path).st_mtime

		if dbObj.changeDate < lastEditTime:

			dbObj.changeDate = lastEditTime

			dbObj.save()

			if fileExtension in [".mp3"]:
				self.HandleAudioFile(path, dbObj)


	def HandleAudioFile(self, path, refdbFile):
		print "Try to handle {0}".format(path)

		fileName, fileExtension = os.path.splitext(path)

		tagObject = None
		if model.AudioFile.objects.filter(refFile=refdbFile).count() == 0:
			tagObject = model.AudioFile()
			tagObject.refFile = refdbFile
			print "Create new mp3 Tag"
		else:
			tagObject = model.AudioFile.objects.filter(refFile=refdbFile)[:1][0]
			print "Load mp3 Tag"

		if fileExtension in handler.audio:
			handlerClass = handler.audio[fileExtension]

			handlerObj = handlerClass()

			handlerObj.UpdateTags(path, tagObject)

			print [tagObject]

		tagObject.save()



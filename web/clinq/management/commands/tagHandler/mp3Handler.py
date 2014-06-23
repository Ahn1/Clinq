import logging
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen import File

import string
import random

import mimetypes



class HandlerMp3:
	def __init__(self):
		pass


	def UpdateTags(self,media,target):
		try:

			audio = ID3(media)

			title = self.GetContentOfTag(audio.getall('TIT2'))
			artist = self.GetContentOfTag(audio.getall('TPE1'))
			album = self.GetContentOfTag(audio.getall('TALB'))
			track = self.GetContentOfTag(audio.getall('TRCK'))

			target.title = self.get_first(title)
			target.artist = self.get_first(artist,artist)
			target.album = self.get_first(album,album)

			try:
				target.track = self.get_first(track,track)
			except Exception, e:
				target.track = "0"
			


			audio = File(media)

			target.length = audio.info.length

			try:
				artwork = audio.tags['APIC:']
				extension = getExtensionFromMime(artwork.mime)

				print "Cover mime: " + artwork.mime
				print "Guess extension: " + extension

				target.setCover(artwork.data, id_generator() + extension)
				target.coverMime = artwork.mime


			except Exception, e:
				print ("Cannot Handle cover: %s" % e)
			

			logging.debug("Tag of '%s' refreshed: %s",media,target)
			
		except Exception,e:
			print e


	def GetContentOfTag(self,tags):
		try:
			return self.get_first([getattr(x,"text") for x in tags])
		except Exception, e:
			return [""]

	def get_first(self,iterable, default=None):
		if iterable:
			for item in iterable:
				return item
		return default



def getExtensionFromMime(mime):
	return mimetypes.guess_extension(mime)

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

	
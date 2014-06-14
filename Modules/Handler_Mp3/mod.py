import logging
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3


def Info():
	return {
		"name": "handler_mp3",
		"version": "0.1"
	}

def Register(app):

	handler = {
		"UpdateTag": GetMP3Tag
	}

	app.RegisterTagHandler(".mp3",handler)

def GetMP3Tag(app,media,target):
	try:

		#audio = ID3(media)

		#print '---------------'
		#print audio.pprint()

		audio = EasyID3(media)

		target["title"] = audio["title"]

		audio = MP3(media)



		target["length"] = audio.info.length

		logging.debug("Tag of '%s' refreshed: %s",media,target)
	except Exception,e:
		logging.error("Cannot get MP3 Tag: %s", e)
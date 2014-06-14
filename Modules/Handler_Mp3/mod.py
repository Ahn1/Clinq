import logging
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3


def Info():
	return {
		"name": "MP3 Tag Handler",
		"version": "0.1"
	}

def Register(app):
	app.RegisterTagHandler(".mp3",GetMP3Tag)

def GetMP3Tag(media,target):
	audio = EasyID3(media)

	target["title"] = audio["title"]


	audio = MP3(media)

	target["length"] = audio.info.length

	logging.debug("Tag of '%s' refreshed: %s",media,target)
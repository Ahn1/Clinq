import logging
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3


def Info():
	return {
		"name": "handler_mp3",
		"version": "0.2",
		"description": "Handler for MP3 tags",
	}

def Register(app):

	handler = {
		"UpdateTag": GetMP3Tag
	}

	app.RegisterTagHandler(".mp3",handler)

def GetMP3Tag(app,media,target):
	try:

		audio = ID3(media)

		title = GetContentOfTag(audio.getall('TIT2'))
		artist = GetContentOfTag(audio.getall('TPE1'))
		album = GetContentOfTag(audio.getall('TALB'))
		track = GetContentOfTag(audio.getall('TRCK'))

		target["title"] = title
		target["artist"] = artist
		target["album"] = album
		target["track"] = track


		audio = MP3(media)

		target["length"] = audio.info.length

		logging.debug("Tag of '%s' refreshed: %s",media,target)
		
	except Exception,e:
		logging.error("Cannot get MP3 Tag: %s", e)


def GetContentOfTag(tags):
	try:
		return get_first([getattr(x,"text") for x in tags])
	except Exception, e:
		return [""]

def get_first(iterable, default=None):
	if iterable:
		for item in iterable:
			return item
	return default
import os
import clinq.models as model

from optparse import make_option
from django.core.management.base import BaseCommand, CommandError

from django.conf import settings

class Command(BaseCommand):
	#option_list = BaseCommand.option_list + (
	#	make_option('--long', '-l', dest='long',
	#		help='Help for the long options'),
	#)
	help = 'List all audio files'

	def handle(self, **options):
		files = model.AudioFile.objects.all().order_by("artist","album","track")

		for audio in files:
			print "----"
			print "Artist: " + audio.artist
			print "Album: " + audio.album
			print "Title: " + audio.title
			print "Track: " + audio.track
			print "Path: " + os.path.join(settings.MEDIA_PATH.decode("utf-8"),audio.refFile.path)
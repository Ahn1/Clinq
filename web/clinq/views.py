from django.shortcuts import render
import clinq.models as model

from django.http import HttpResponse, StreamingHttpResponse

from django.db.models import Count, Min, Sum, Avg

from django.shortcuts import get_object_or_404, render

# Create your views here.


def Home(request):
	return render(request, 'home.html', None)


def audio_by_Artists(request):
	groupes = model.AudioFile.objects.order_by("artist").values("artist").annotate(totalLength=Sum('length'))

	return render(request, 'musik_by_artist.html', {"artists": groupes})


def list_albums(request):
	
	def getAllAlbums():
		groupes = model.AudioFile.objects.order_by("artist","album").values("artist","album").annotate(totalLength=Sum('length'))
		for g in groupes:
			yield ("%s\n"%g)

	resp = StreamingHttpResponse( getAllAlbums(), mimetype='text/plain')
	return resp

def list_artists(request):
	def getAllArtists():
		groupes = model.AudioFile.objects.order_by("artist").values("artist").annotate(totalLength=Sum('length'))
		for g in groupes:
			yield ("%s\n"%g)

	resp = StreamingHttpResponse( getAllArtists(), mimetype='text/plain')
	return resp

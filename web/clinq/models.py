from django.db import models


class File(models.Model):
	path = models.CharField(max_length=300, db_index=True, default="")
	changeDate = models.FloatField(default=0)
		

# Create your models here.
class AudioFile(models.Model):
	title = models.CharField(max_length=200, db_index=True, default="")
	album = models.CharField(max_length=200, db_index=True, default="")
	artist = models.CharField(max_length=200,db_index=True, default="")
	length = models.FloatField(default=0)
	track = models.CharField(max_length=10)
	lastEdited = models.DateTimeField('date published', db_index=True,auto_now=True)

	refFile = models.OneToOneField(File, primary_key=True)

	def __unicode__(self):
		return self.title

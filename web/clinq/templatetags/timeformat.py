from django import template

register = template.Library()

@register.filter
def dispalayTime(value):
	hours = int(value / 60 / 60)
	minutes = int((value / 60) % 60)

	return str(hours) + ":" + str(minutes).zfill(2)

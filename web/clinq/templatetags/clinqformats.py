from django import template
import base64

from django.utils.encoding import smart_str

register = template.Library()

@register.filter
def HexEncode(value):
	code = smart_str(value).encode('hex')

	return code


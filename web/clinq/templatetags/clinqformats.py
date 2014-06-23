from django import template
import base64

from django.utils.encoding import smart_str

import clinq.models as model

register = template.Library()

@register.filter
def HexEncode(value):
	code = smart_str(value).encode('hex')

	return code

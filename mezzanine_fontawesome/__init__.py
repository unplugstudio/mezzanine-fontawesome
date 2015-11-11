from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Icon(object):

    def __init__(self, icon_name):
        self.name = icon_name

    def __str__(self):
        return self.name

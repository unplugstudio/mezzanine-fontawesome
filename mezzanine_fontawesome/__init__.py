from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Icon(object):

    def __init__(self, icon_name):
        # Trim surrounding whitespace
        self.name = ",".join(s.strip() for s in icon_name.split(","))

    def __str__(self):
        return self.name

    def get_icon_display(self):
        return self.name.split(",")[0]

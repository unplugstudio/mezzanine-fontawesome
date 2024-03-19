from __future__ import unicode_literals

from django import forms

from . import Icon
from .widgets import IconWidget


class IconFormField(forms.Field):

    def __init__(self, *args, **kwargs):
        self.widget = IconWidget

        if "initial" in kwargs:
            kwargs["initial"] = Icon(*kwargs["initial"])

        super(IconFormField, self).__init__(**kwargs)

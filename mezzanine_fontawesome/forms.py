from __future__ import unicode_literals

from django import forms

from . import Icon
from widgets import IconWidget


class IconFormField(forms.Field):

    def __init__(self, *args, **kwargs):
        self.widget = IconWidget

        if 'initial' in kwargs:
            kwargs['initial'] = Icon(*kwargs['initial'])

        super(IconFormField, self).__init__(**kwargs)

    def widget_attrs(self, widget):
        classes = widget.attrs.get('class', '').split()
        classes.append('fontawesome-select')

        return {
            'class': ' '.join(classes),
        }

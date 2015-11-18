from __future__ import unicode_literals

from django import forms

from utils import get_icon_choices_and_filters

CHOICES = get_icon_choices()


class Select2Widget(forms.Select):

    def __init__(self, attrs=None):
        attrs = {"class": "select2-widget"}
        super(Select2Widget, self).__init__(attrs)

    class Media:
        js = (
            'fontawesome/js/django_fontawesome.js',
            "//cdnjs.cloudflare.com/ajax/libs/select2/4.0.1-rc.1/js/select2.full.min.js"
        )
        css = {
            "all": (
                "//cdnjs.cloudflare.com/ajax/libs/select2/4.0.1-rc.1/"
                "css/select2.min.css",
            )
        }


class IconWidget(Select2Widget):

    def __init__(self, attrs=None):
        attrs = {"class": "fontawesome-select"}
        super(Select2Widget, self).__init__(attrs, choices=CHOICES)

    class Media:
        css = {
            'all': (
                '//maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css',
            )
        }

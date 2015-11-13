from __future__ import unicode_literals

from django import forms

from utils import get_icon_choices_and_filters

CHOICES, icon_filters = get_icon_choices_and_filters()


class IconWidget(forms.Select):

    def __init__(self, attrs=None):
        attrs = {'class': 'fontawesome-select'}
        super(IconWidget, self).__init__(attrs, choices=CHOICES)

    class Media:
        js = (
            'fontawesome/js/django_fontawesome.js',
            "//cdnjs.cloudflare.com/ajax/libs/select2/4.0.1-rc.1/js/select2.full.min.js"
        )

        css = {
            'all': (
                '//maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css',
                '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.1-rc.1/css/select2.min.css'
            )
        }

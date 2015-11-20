from __future__ import unicode_literals

from django import forms

from utils import get_icon_choices

CHOICES = get_icon_choices()


class Select2Widget(forms.Select):

    def build_attrs(self, extra_attrs=None, **kwargs):
        """
        Add data attributes for the select2 widget.
        """
        attrs = super(Select2Widget, self).build_attrs(extra_attrs=extra_attrs, **kwargs)
        if "class" in attrs:
            attrs["class"] += " select2-widget"
        else:
            attrs["class"] = "select2-widget"
        return attrs

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
        super(IconWidget, self).__init__(attrs, choices=CHOICES)

    def build_attrs(self, extra_attrs=None, **kwargs):
        """
        Add data attributes for the icon fontawesome widget.
        """
        attrs = super(Select2Widget, self).build_attrs(extra_attrs=extra_attrs, **kwargs)
        if "class" in attrs:
            attrs["class"] += " fontawesome-select"
        else:
            attrs["class"] = "fontawesome-select"
        return attrs

    class Media:
        css = {
            'all': (
                '//maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css',
            )
        }

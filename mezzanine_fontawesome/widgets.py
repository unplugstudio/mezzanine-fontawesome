from __future__ import unicode_literals

from django import forms
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from utils import get_icon_choices_and_filters

CHOICES, icon_filters = get_icon_choices_and_filters()


class IconWidget(forms.Select):

    def __init__(self, attrs=None):
        super(IconWidget, self).__init__(attrs, choices=CHOICES)

    def render_option(self, selected_choices, option_value, option_label):
        if option_value is None:
            option_value = ''
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''

        filters = icon_filters[option_value]
        if filters is not None:
            filters = mark_safe('data-icon-filter="' + ' '.join(filters) + '"')
        else:
            filters = ''

        return format_html(
            '<option data-icon-name="{0}" {3} value="{0}"{1}>{2}</option>',
            option_value,
            selected_html,
            force_text(option_label),
            filters,
        )

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

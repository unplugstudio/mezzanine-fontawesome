from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from . import Icon
from .forms import IconFormField


class IconField(models.Field):

    description = _("A fontawesome icon field")

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 60
        super(IconField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return Icon(icon_name=value)

    def to_python(self, value):
        if value is None:
            return value

        if isinstance(value, Icon):
            return value

        return Icon(icon_name=value)

    def get_internal_type(self):
        return "CharField"

    def get_prep_value(self, value):
        return str(value)

    def formfield(self, **kwargs):
        defaults = {
            "form_class": IconFormField,
        }
        defaults.update(kwargs)
        return super(IconField, self).formfield(**defaults)

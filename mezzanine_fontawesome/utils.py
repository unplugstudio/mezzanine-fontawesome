import os
import json

# Converted from https://github.com/FortAwesome/Font-Awesome/blob/master/src/icons.yml
PATH = os.path.join(os.path.dirname(__file__), "static/fontawesome/js/icons.json")


def get_icon_choices_and_filters():

    CHOICES = [("", "----------")]
    icon_filters = {"": ["----------"]}

    with open(PATH) as f:
        icons = json.load(f)

    for icon in icons.get("icons"):
        CHOICES.append((
            icon.get("id"),
            icon.get("text")
        ))

        icon_filters[icon.get("id")] = icon.get("filter")

    return CHOICES, icon_filters

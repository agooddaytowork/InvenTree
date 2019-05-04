""" This module provides template tags for extra functionality
over and above the built-in Django tags.
"""

from django import template
from InvenTree import version

register = template.Library()


@register.simple_tag()
def multiply(x, y, *args, **kwargs):
    """ Multiply two numbers together """
    return x * y


@register.simple_tag()
def inventree_version(*args, **kwargs):
    """ Return InvenTree version string """
    return version.inventreeVersion()


@register.simple_tag()
def inventree_commit(*args, **kwargs):
    """ Return InvenTree git commit hash string """
    return version.inventreeCommitHash()


@register.simple_tag()
def inventree_github(*args, **kwargs):
    """ Return URL for InvenTree github site """
    return "https://github.com/InvenTree"

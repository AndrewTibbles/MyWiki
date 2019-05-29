from django import template
import markdown, re

register = template.Library()

charExclusion = re.compile(r"\[\[([A-Za-z0-9_%]+)\]\]") # Allowed values for use in the page title.

# Used as part of my intergration for markdown
@register.filter
def markup(text):
    return markdown.markdown(text)

# Registers a filter for page creations to only accept the characters provided by `charExlusion`
@register.filter
def titleValidator(text):
    return charExclusion.sub(r'''
    <a href="../\1/">\1</a>
    ''', text)
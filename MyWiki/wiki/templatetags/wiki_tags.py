from django import template
import markdown, re

register = template.Library()

charExclusion = re.compile(r"\[\[([A-Za-z0-9_%]+)\]\]")

@register.filter
def markup(text):
    return markdown.markdown(text)

@register.filter
def titleValidator(text):
    return charExclusion.sub(r'''
    <a href="../\1/">\1</a>
    ''', text)
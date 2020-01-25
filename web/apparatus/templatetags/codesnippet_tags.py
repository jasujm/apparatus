from django import template
from django.utils.html import format_html

register = template.Library()


@register.inclusion_tag("apparatus/include/hlscript.html", takes_context=True)
def hlscript(context):
    pl = context["instance"].programming_language
    return {
        "cdn_base_url": context["cdn_base_url"],
        "filename": f"languages/{pl.code}.min.js",
        "is_external": pl.is_external,
        "subresource_integrity_hash": pl.subresource_integrity_hash,
    }

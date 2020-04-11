from django import template

from django.conf import settings

register = template.Library()


@register.inclusion_tag("apparatus/include/blog_comments.html", takes_context=True)
def comment_section(context):
    return {
        "apparatus_site": settings.APPARATUS_DISQUS_SITE,
        "page_url": context["meta"].url,
        "page_identifier": context["post"].guid,
    }

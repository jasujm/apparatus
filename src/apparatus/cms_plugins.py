from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import CodeSnippet, FalsePositiveDemo


@plugin_pool.register_plugin
class CodeSnippetPlugin(CMSPluginBase):
    module = _("Apparatus")
    name = _("Code snippet")
    model = CodeSnippet
    text_enabled = True
    render_template = "apparatus/codesnippet.html"
    fields = ["programming_language", "body"]

    @classmethod
    def get_render_queryset(cls):
        return super().get_render_queryset().select_related("programming_language")


@plugin_pool.register_plugin
class FalsePositiveDemoPlugin(CMSPluginBase):
    module = _("Apparatus")
    name = _("False positive demo")
    model = FalsePositiveDemo
    text_enabled = True
    render_template = "apparatus/fpdemo.html"

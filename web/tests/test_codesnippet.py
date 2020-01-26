from cms.api import add_plugin
from cms.models import Placeholder
from django.test import TestCase

from apparatus import models, cms_plugins, settings
from apparatus.templatetags import codesnippet_tags


class CodeSnippetTest(TestCase):
    def testCodeSnippetRenderHlscriptTag(self):
        programming_language = models.ProgrammingLanguage.objects.create(
            code="cpp", name="C++"
        )
        snippet = models.CodeSnippet.objects.create(
            programming_language=programming_language, body="int main() {}"
        )
        self.assertEqual(
            codesnippet_tags.hlscript(
                {"cdn_base_url": "localhost", "instance": snippet,}
            ),
            {
                "cdn_base_url": "localhost",
                "filename": "languages/cpp.min.js",
                "is_external": False,
                "subresource_integrity_hash": "",
            },
        )

    def testCodeSnippetRenderPlugin(self):
        placeholder = Placeholder.objects.create(slot="test")
        model_instance = add_plugin(placeholder, cms_plugins.CodeSnippetPlugin, "en",)
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)
        self.assertEqual(
            context.get("cdn_base_url"), settings.APPARATUS_CODESNIPPET_CDN_BASE_URL
        )

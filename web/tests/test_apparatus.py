from django.test import TestCase
from cms.api import add_plugin
from cms.models import Placeholder

from apparatus import models, cms_plugins, settings
from apparatus.templatetags import codesnippet_tags


def _get_test_programming_language():
    return models.ProgrammingLanguage.objects.get_or_create(
        code="cpp", defaults={"name": "C++"}
    )[0]


class ProgrammingLanguageTest(TestCase):
    def testDisplay(self):
        self.assertEqual(str(_get_test_programming_language()), "C++ (cpp)")


class CodeSnippetTest(TestCase):
    def testCodeSnippetRenderHlscriptTag(self):
        programming_language = _get_test_programming_language()
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

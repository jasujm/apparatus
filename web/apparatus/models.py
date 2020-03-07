from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProgrammingLanguage(models.Model):
    code = models.CharField(_("Code"), max_length=15, unique=True)
    name = models.CharField(_("Name"), max_length=63)
    is_external = models.BooleanField(_("Is external resource"), default=False)
    subresource_integrity_hash = models.CharField(
        _("Subresource integrity hash"), max_length=64, blank=True
    )

    class Meta:
        verbose_name = _("programming language")
        verbose_name_plural = _("programming languages")

    def __str__(self):
        return f"{self.name} ({self.code})"


class CodeSnippet(CMSPlugin):
    programming_language = models.ForeignKey(
        ProgrammingLanguage, on_delete=models.PROTECT, blank=True, null=True
    )
    body = models.TextField(_("Body"))

    class Meta:
        verbose_name = _("code snippet")
        verbose_name_plural = _("code snippets")

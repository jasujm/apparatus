from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProgrammingLanguage(models.Model):
    code = models.CharField(_("Code"), max_length=15, unique=True)
    name = models.CharField(_("Name"), max_length=63)

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


class FalsePositiveDemo(CMSPlugin):
    prevalence = models.FloatField(_("Prevalence"))
    sensitivity = models.FloatField(_("Sensitivity"))
    specificity = models.FloatField(_("Specificity"))

    @property
    def prevalence_percentage(self):
        return int(100 * self.prevalence)

    class Meta:
        verbose_name = _("false positives demo")
        verbose_name_plural = _("false positives demos")

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

class ProgrammingLanguage(models.Model):
    code = models.CharField(_("Code"), max_length=15, unique=True)
    name = models.CharField(_("Name"), max_length=63)

    def __str__(self):
        return f"{self.name} ({self.code})"

class CodeSnippet(CMSPlugin):
    programming_language = models.ForeignKey(ProgrammingLanguage, on_delete=models.PROTECT, blank=True, null=True)
    body = models.TextField(_("Body"))

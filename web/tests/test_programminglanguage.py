from django.test import TestCase

from apparatus import models


class ProgrammingLanguageTest(TestCase):
    def testDisplay(self):
        programming_language = models.ProgrammingLanguage.objects.create(
            code="cpp", name="C++"
        )
        self.assertEqual(str(programming_language), "C++ (cpp)")

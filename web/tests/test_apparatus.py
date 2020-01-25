from django.test import TestCase
from apparatus import models


class ProgrammingLanguageTest(TestCase):
    def setUp(self):
        self.programming_language = models.ProgrammingLanguage.objects.create(
            code="cpp", name="C++"
        )

    def testDisplay(self):
        self.assertEqual(str(self.programming_language), "C++ (cpp)")

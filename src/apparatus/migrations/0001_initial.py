# Generated by Django 2.2.9 on 2020-01-11 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProgrammingLanguage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(max_length=15, unique=True, verbose_name="Code"),
                ),
                ("name", models.CharField(max_length=63, verbose_name="Name")),
            ],
        ),
        migrations.CreateModel(
            name="CodeSnippet",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="apparatus_codesnippet",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("body", models.TextField(verbose_name="Body")),
                (
                    "programming_language",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="apparatus.ProgrammingLanguage",
                    ),
                ),
            ],
            options={"abstract": False,},
            bases=("cms.cmsplugin",),
        ),
    ]

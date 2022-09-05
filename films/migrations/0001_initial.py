# Generated by Django 4.1 on 2022-09-05 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FilmsCatalog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField(blank=True)),
                ("genre", models.CharField(max_length=100)),
                ("raiting", models.CharField(max_length=10)),
                ("url_youtube", models.URLField(max_length=500)),
                ("utl_image_preview", models.URLField(max_length=500)),
                ("release_year", models.CharField(max_length=10)),
                ("mark", models.CharField(max_length=10)),
            ],
        ),
    ]
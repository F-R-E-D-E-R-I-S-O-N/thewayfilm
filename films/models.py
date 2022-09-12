from django.db import models

class FilmsCatalog(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.TextField(blank=True)
    content = models.TextField(blank=True)
    genre = models.CharField(max_length=100)
    raiting = models.CharField(max_length=10)
    url_youtube = models.URLField(max_length=500)
    url_image_preview = models.URLField(max_length=500)
    title_for_url = models.URLField(max_length=30, default='#') 
    release_year = models.CharField(max_length=10)
    mark = models.CharField(max_length=10) # film, poster, trailer
    new_film = models.BooleanField(default=False)

    def __str__(self):
        return self.title

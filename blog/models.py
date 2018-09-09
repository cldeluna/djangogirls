from django.db import models
from django.utils import timezone

# Create your models here.

GENRES = (
    ('satire','Satire'),
    ('poetry','Poetry'),
    ('horror','Horror'),
    ('auto','Autobiographical')
)


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    genre = models.CharField('Genre', max_length=24,
            choices=GENRES, default=GENRES[0][0])
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

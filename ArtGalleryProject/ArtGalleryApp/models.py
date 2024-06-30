from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class ArtExhibition(models.Model):
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    description = models.TextField(max_length=200)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} - {self.location}"

    def get_art_pieces(self):
        return ArtPiece.objects.filter(art_exhibition=self)


class Artist(models.Model):
    ART_STYLES = [
        ("impressionism", "impressionism"),
        ("pop art", "pop art"),
        ("graffiti", "graffiti")
    ]

    full_name = models.CharField(max_length=50)
    art_style = models.CharField(max_length=30, choices=ART_STYLES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name} - {self.art_style}"


class ArtPiece(models.Model):
    title = models.CharField(max_length=50)
    creation_date = models.DateField()
    image = models.ImageField(upload_to='artpieces/')
    art_exhibition = models.ForeignKey(ArtExhibition, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.artist}"

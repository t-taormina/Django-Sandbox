from django.db import models

# Create your models here.


class Golfer(models.Model):
    golfer = models.CharField(max_length=200)
    score = models.IntegerField()

    def __str__(self):
        return self.golfer


class Player(models.Model):
    player = models.CharField(max_length=200)
    golfers = models.ManyToManyField(Golfer)

    def __str__(self):
        return self.player







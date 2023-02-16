from django.db import models

class Director(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Elprimo(models.Model):
    name = models.CharField(max_length=45)
    des = models.TextField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Elprimo, on_delete=models.CASCADE)
    def __str__(self):
        return self.text

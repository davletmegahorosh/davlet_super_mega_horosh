from django.db import models

class Director(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name


# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

# class Tag(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

class Elprimo(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    # tag = models.ManyToManyField(Tag, blank=True)
    name = models.CharField(max_length=45)
    des = models.TextField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    # def category_name(self):
    #     try:
    #         return self.category.name
    #     except:
    #         return ''

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Elprimo, on_delete=models.CASCADE, null=True, related_name='elprimo_reviews')
    stars = models.IntegerField(choices=(
        (1,'*'),
        (2, '* *'),
        (3, '* * *'),
        (4, '* * * *'),
        (5, '* * * * *'),
    ),default = 5)
    def __str__(self):
        return self.text
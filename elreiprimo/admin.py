from django.contrib import admin
from .models import Elprimo, Director, Review

admin.site.register(Elprimo)
admin.site.register(Review)
admin.site.register(Director)
# admin.site.register(Category)
# admin.site.register(Tag)
from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from API import models

admin.site.register(models.Book)
admin.site.register(models.Press)
admin.site.register(models.Author)
admin.site.register(models.AuthorDetail)

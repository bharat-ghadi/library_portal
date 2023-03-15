from django.contrib import admin
from .models import Genre, BookData, UserData, Workspace

# Register your models here.

admin.site.register(Genre)
admin.site.register(BookData)
admin.site.register(UserData)
admin.site.register(Workspace)

from django.contrib import admin
from boards.models import Post, Topic, Board
# Register your models here.
admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)

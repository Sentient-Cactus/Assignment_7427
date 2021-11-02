from django.contrib import admin

# Register your models here.
from blog.models import Dog, Activity, Breed, Comment

admin.site.register(Dog)
admin.site.register(Activity)
admin.site.register(Breed)
admin.site.register(Comment)
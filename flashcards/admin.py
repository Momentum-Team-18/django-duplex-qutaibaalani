# Import the sub function from the re module
from re import sub

# Import the admin module
from django.contrib import admin

# Import the models
from .models import Flashcard, User, Subject

# Register your models here.

# Register the User model with the admin site
admin.site.register(User)
# Register the Subject model with the admin site
admin.site.register(Subject)
# Register the Flashcard model with the admin site
admin.site.register(Flashcard)

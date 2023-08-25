# Import the AppConfig class
from django.apps import AppConfig


# Define the FlashcardsConfig class
class FlashcardsConfig(AppConfig):
    # Specify the default auto field
    default_auto_field = "django.db.models.BigAutoField"
    # Specify the name of the app
    name = "flashcards"

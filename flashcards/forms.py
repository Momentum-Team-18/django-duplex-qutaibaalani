# Import the forms module
from django import forms

# Import the models
from .models import Flashcard, Subject


# Define the SubjectForm class
class SubjectForm(forms.ModelForm):
    class Meta:
        # Specify the Subject model
        model = Subject
        # Specify the form fields
        fields = ("subject",)


# Define the FlashcardForm class
class FlashcardForm(forms.ModelForm):
    class Meta:
        # Specify the Flashcard model
        model = Flashcard
        # Specify the form fields
        fields = (
            "question",
            "answer",
        )

# Import the TRUE constant from the pickle module
from pickle import TRUE

# Import the AbstractUser class
from django.contrib.auth.models import AbstractUser as BaseUser

# Import the models module
from django.db import models


# Create your models here.


# Define the User model
class User(BaseUser):
    pass


# Define the Subject model
class Subject(models.Model):
    # Define the subject field
    subject = models.CharField(max_length=200)
    # Define the user field as a foreign key
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subjects", null=TRUE
    )

    # Define the string representation of the Subject model
    def __str__(self):
        return f"{self.subject}"


# Define the Flashcard model
class Flashcard(models.Model):
    # Define the subject field as a foreign key
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="flashcards"
    )
    # Define the question field
    question = models.TextField()
    # Define the answer field
    answer = models.TextField()

    # Define the string representation of the Flashcard model
    def __str__(self):
        return f"{self.question}, {self.answer}"

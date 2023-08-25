# Import the path function from django.urls
from django.urls import path

# Import the views module from the current package
from . import views

urlpatterns = [
    # Define a URL pattern for listing subjects
    path("", views.list_subject, name="list_subject"),
    # Define a URL pattern for creating a new subject
    path("subject/new/", views.subject_new, name="subject_new"),
    # Define a URL pattern for editing a subject
    path("subject/edit/<int:pk>", views.subject_edit, name="subject_edit"),
    # Define a URL pattern for deleting a subject
    path("delete_subject/<int:pk>", views.delete_subject, name="delete_subject"),
    # Define a URL pattern for viewing flashcard questions
    path("card_questions/<int:pk>", views.card_questions, name="card_questions"),
    # Define a URL pattern for viewing a flashcard answer
    path("card_answer/<int:pk1>", views.card_answer, name="card_answer"),
    # Define a URL pattern for creating a new flashcard
    path("flashcard/new/<int:pk>", views.card_new, name="card_new"),
    # Define a URL pattern for editing a flashcard
    path("flashcard/edit/<int:pk1>/<int:pk2>", views.card_edit, name="card_edit"),
    # Define a URL pattern for deleting a flashcard
    path("delete_card/<int:pk1>/<int:pk2>", views.delete_card, name="delete_card"),
]

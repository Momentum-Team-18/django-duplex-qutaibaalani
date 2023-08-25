# Import the NONE constant from the pickle module
from pickle import NONE

# Import the render and get_object_or_404 functions from django.shortcuts
from django.shortcuts import render, get_object_or_404

# Import the flashcards module
import flashcards

# Import the Flashcard and Subject models from flashcards.models
from flashcards.models import Flashcard, Subject

# Import the SubjectForm and FlashcardForm from the current package
from .forms import SubjectForm, FlashcardForm

# Import the redirect function from django.shortcuts
from django.shortcuts import redirect

# Import the login_required decorator from django.contrib.auth.decorators
from django.contrib.auth.decorators import login_required

# Create your views here.


# Apply the login_required decorator to the view
@login_required
def list_subject(request):
    # Retrieve subjects for the current user
    subjects = Subject.objects.filter(user=request.user)
    return render(request, "flashcards/list_subject.html", {"subjects": subjects})


# Apply the login_required decorator to the view
@login_required
def subject_new(request):
    if request.method == "POST":
        # Create a new SubjectForm instance with the submitted data
        subject_form = SubjectForm(request.POST)
        if subject_form.is_valid():
            # Save the subject form data to a new Subject instance
            subject = subject_form.save(commit=False)
            # Set the user of the subject to the current user
            subject.user = request.user
            # Save the subject instance
            subject.save()
            # Redirect to the list_subject view
            return redirect("list_subject")
    else:
        # Create a new empty SubjectForm instance
        subject_form = SubjectForm()
    return render(
        # Render the subject_new.html template with the subject_form
        request,
        "flashcards/subject_new.html",
        {"subject_form": subject_form},
    )


# Apply the login_required decorator to the view
@login_required
def subject_edit(request, pk):
    # Get the subject instance with the specified pk or show a 404 error
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        # Create a SubjectForm instance with the submitted data and the existing subject instance
        subject_form = SubjectForm(request.POST, instance=subject)
        if subject_form.is_valid():
            # Save the subject form data to the existing subject instance
            subject = subject_form.save(commit=False)
            # Save the subject instance
            subject.save()
            # Redirect to the list_subject view
            return redirect("list_subject")
    else:
        # Create a SubjectForm instance with the existing subject instance
        subject_form = SubjectForm(instance=subject)
    return render(
        # Render the subject_edit.html template with the subject_form
        request,
        "flashcards/subject_edit.html",
        {"subject_form": subject_form},
    )


# Apply the login_required decorator to the view
@login_required
def card_questions(request, pk):
    ## Get the subject instance with the specified pk or show a 404 error
    subject = get_object_or_404(Subject, pk=pk)
    # Retrieve all flashcards associated with the subject
    flashcards = subject.flashcards.all()
    # Render the card_questions.html template with the flashcards and subject
    return render(
        request,
        "flashcards/card_questions.html",
        {"flashcards": flashcards, "subject": subject},
    )


# Apply the login_required decorator to the view
@login_required
def delete_subject(request, pk):
    # Get the subject instance with the specified pk or show a 404 error
    subject = get_object_or_404(Subject, pk=pk)
    # Delete the subject instance
    subject.delete()
    # Redirect to the list_subject view
    return redirect("list_subject")


# Apply the login_required decorator to the view
@login_required
def card_new(request, pk=None):
    # Get the subject instance with the specified pk or show a 404 error
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        # Create a new FlashcardForm instance with the submitted data
        card_form = FlashcardForm(request.POST)
        if card_form.is_valid():
            # Save the flashcard form data to a new Flashcard instance
            card = card_form.save(commit=False)
            # Set the subject of the flashcard to the current subject
            card.subject = subject
            # Save the flashcard instance
            card.save()
            # Redirect to the card_questions view
            return redirect("card_questions", pk=pk)
    else:
        # Create a new empty FlashcardForm instance
        card_form = FlashcardForm()
        # Render the card_new.html template with the card_form
    return render(request, "flashcards/card_new.html", {"card_form": card_form})


# Apply the login_required decorator to the view
@login_required
def card_edit(request, pk1, pk2):
    # Get the flashcard instance with the specified pk or show a 404 error
    card = get_object_or_404(Flashcard, pk=pk1)
    # Get the subject instance with the specified pk or show a 404 error
    subject = get_object_or_404(Subject, pk=pk2)
    if request.method == "POST":
        # Create a FlashcardForm instance with the submitted data and the existing flashcard instance
        card_form = FlashcardForm(request.POST, instance=card)
        if card_form.is_valid():
            # Save the flashcard form data to the existing flashcard instance
            card = card_form.save(commit=False)
            # Set the subject of the flashcard to the current subject
            card.subject = subject
            # Set the user of the flashcard to the current user
            card.user = request.user
            # Save the flashcard instance
            card.save()
            # Redirect to the card_questions view
            return redirect("card_questions", pk=pk2)
    else:
        # Create a FlashcardForm instance with the existing flashcard instance
        card_form = FlashcardForm(instance=card)
        # Render the card_edit.html template with the card_form
    return render(request, "flashcards/card_edit.html", {"card_form": card_form})


# Apply the login_required decorator to the view
@login_required
def delete_card(request, pk1, pk2):
    # Get the flashcard instance with the specified pk or show a 404 error
    card = get_object_or_404(Flashcard, pk=pk1)
    # Delete the flashcard instance
    card.delete()
    # Get the subject instance with the specified pk or show a 404 error
    subject = get_object_or_404(Subject, pk=pk2)
    # Redirect to the card_questions view
    return redirect("card_questions", pk=pk2)


def card_answer(request, pk1):
    # Get the flashcard instance with the specified pk or show a 404 error
    card = get_object_or_404(Flashcard, pk=pk1)
    # Render the card_answer.html template with the card
    return render(request, "flashcards/card_answer.html", {"card": card})

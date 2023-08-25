"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Import the admin module
from django.contrib import admin

# Import the path and include functions
from django.urls import path, include


urlpatterns = [
    # Set the admin URL
    path("admin/", admin.site.urls),
    # Include URLs for the simple registration backend
    path("accounts/", include("registration.backends.simple.urls")),
    # Include URLs for the flashcards app
    path("", include("flashcards.urls")),
]

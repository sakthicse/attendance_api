"""urlconf for the base application"""

from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path('', login_required(views.Home.as_view()), name='home'),
]
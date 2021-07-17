from django.urls import path
from .views import HomePageView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
]

from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import Book


class HomePageView(TemplateView):
    model = Book
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['featured'] = Book.objects.all().order_by("title")[:3]
        return context

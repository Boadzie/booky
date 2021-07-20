from django.urls import path
from .views import BookListView, BookDetailView, SearchResultsListView

urlpatterns = [
    path('', BookListView.as_view(), name="books"),
    path('<uuid:pk>/', BookDetailView.as_view(), name="book"),
    path('search/', SearchResultsListView.as_view(), name='search_results')
]

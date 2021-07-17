
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # User management
    path('accounts/', include('allauth.urls')),

    # Local apps
    path('accounts/', include('accounts.urls')),
    # pages views
    path('', include('pages.urls')),
]

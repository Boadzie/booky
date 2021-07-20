
from django.contrib import admin
from django.conf import settings  # new
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # User management
    path('accounts/', include('allauth.urls')),

    # Local apps
    path('accounts/', include('accounts.urls')),
    # pages views
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

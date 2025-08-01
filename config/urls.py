from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line includes all the URLs from your 'core' app
    path('api/', include('core.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# This is important for serving images/files you upload in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
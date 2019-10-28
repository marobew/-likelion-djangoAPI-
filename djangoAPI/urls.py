from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
import rest_framework.urls
import Essay.urls
import File.urls
import Album.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('file', include(File.urls)),
    path('album', include(Album.urls)),
    path('essay', include(Essay.urls)),
    path('api-auth/', include(rest_framework.urls)),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
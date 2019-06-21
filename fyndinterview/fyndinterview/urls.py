

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from api import urls as urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^imdb/', include(urls, namespace='api')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

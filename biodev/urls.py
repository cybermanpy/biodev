from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('usersinfo.urls', namespace='usersinfo')),
    url(r'^', include('checks.urls', namespace='checks')),
    url(r'^', include('payobjects.urls', namespace='payobjects')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

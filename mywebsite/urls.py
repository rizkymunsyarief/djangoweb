from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'webaci/',include('webaci.urls',namespace='webaci')),
    url(r'^admin/', admin.site.urls),
]

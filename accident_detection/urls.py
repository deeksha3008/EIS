from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^accident_avoidance/', include('accident_avoidance.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('accident_avoidance.urls'))
]

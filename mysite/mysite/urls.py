from django.conf.urls import url
from django.contrib import admin
from .views import index 
from .views import current_datetime
from .views import hours_ahead 

urlpatterns = [
	
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^time/$', current_datetime),
	url(r'^$', index),
    url(r'^admin/', admin.site.urls),
]

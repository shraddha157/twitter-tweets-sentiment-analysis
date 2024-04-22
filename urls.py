from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.button),
    path('twt',views.twt,name='home-page'),
    path('sa',views.sa,name='sentiment'),
    path('',views.value),
]
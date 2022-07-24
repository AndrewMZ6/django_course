from django.contrib import admin
from django.urls import path, include
from polls import urls
from polls.views import real_index

urlpatterns = [
    path('', real_index),
    path('admin/', admin.site.urls),
    path('polls/', include(urls)),
]

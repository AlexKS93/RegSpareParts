from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from reg.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    #path('users/', include('users.urls')),
    path('', index),
    #path('/', include('reg.urls')),
]

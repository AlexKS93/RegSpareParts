from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from reg.views import index, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/', include('users.urls')),
    path('', index),
    path('login/', login)
    #path('/', include('reg.urls')),
]

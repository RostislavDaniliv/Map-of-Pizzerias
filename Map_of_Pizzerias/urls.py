from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('pizzerias', ListCreatePizzerias.as_view(), name='list_pizzerias')
]

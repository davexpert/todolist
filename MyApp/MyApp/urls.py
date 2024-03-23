from django.contrib import admin
from django.urls import path, include

from testapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls')),

]

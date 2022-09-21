from django.comtrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
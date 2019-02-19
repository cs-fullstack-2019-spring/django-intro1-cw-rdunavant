from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('music/', admin.site.urls),
    path('REM/', admin.site.urls),
    path('ThePolice/', admin.site.urls),
    path('Three6Mafia/', admin.site.urls),
]
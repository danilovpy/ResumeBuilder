from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/<int:pk>', views.resume, name='resume'),
    path('resume/<int:pk>/download', views.download_link, name='download'),

]

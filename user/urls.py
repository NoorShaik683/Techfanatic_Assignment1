from .views import image_request  
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
#app_name = 'user'  
urlpatterns = [  
    path('', image_request, name = "image-request"), 
    path('', views.index, name ='index'),
]


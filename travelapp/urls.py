from .import views
from django.urls import path

urlpatterns = [
    # path('', views.displaymessage,name='displaymessage'),
    path('',views.home,name='home')
]

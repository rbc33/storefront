from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.HelloView.as_view()),
    path('hi/', views.HiView.as_view()),        #for test caching  
]

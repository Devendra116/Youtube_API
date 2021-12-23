from django.urls import path
from . import views

#URL config
urlpatterns = [
    path('',views.display_video)
]


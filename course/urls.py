from django.urls import path
from . import views


urlpatterns=[
    path("welcome/",views.welcome),
    path('listView/',views.studentListView.as_view())
]
from django.urls import path
from . import views


app_name = "index"


urlpatterns = [
    path("", views.index, name="home"),
    path("volunteer/", views.volunteer, name="volunteer"),
    path("messageboard/", views.messageboard, name="messageboard"),
    path('messageboard/<int:topic_id>/', views.topic, name='topic'), 
    path("contact/", views.contact, name="contact"),
    path("help/", views.help, name="help"),
    path("donate/", views.donate, name="donate"),
]

from django.urls import path
from .views import kun_uz , PostCreate

urlpatterns = [
    path('add/', PostCreate.as_view() , name = "post-create"),
    path('kun/',kun_uz , name ="kun_uz")
]
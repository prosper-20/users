from django.urls import path
from .views import CreateUserView       # APP URL

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register")
]
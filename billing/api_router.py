from django.urls import path, include
from billing.views.auth import APIRegistrationView, APILoginView


auth_urls = [
    path("register/", APIRegistrationView.as_view(), name="register"),
    path("login/", APILoginView.as_view(), name="login"),
]

urlpatterns = [
    path("auth/", include(auth_urls)),
]
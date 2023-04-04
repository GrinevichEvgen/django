from django.contrib.auth.views import LoginView

from api.users.views import RegistertView
from django.urls import include, path
from rest_framework import routers
from api.products.views import ProductViewSet
from api.users.views import RegisterView, LoginView

app_name = "api"

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]


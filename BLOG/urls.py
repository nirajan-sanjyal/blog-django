
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("blog_app.urls")),
    path("accounts/login/",views.LoginView.as_view(), name="login"),
    path("accounts/logout/",views.LogoutView.as_view(), name="logout"),
]
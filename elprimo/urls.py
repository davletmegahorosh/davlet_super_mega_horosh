"""elprimo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from elreiprimo.views import elprimo_views, directors_views, reviews_views
from elprimo_user import views as el_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', elprimo_views.TestAPIView.as_view()),

    path('api/v1/elprimos/', elprimo_views.ElprimoListAPIView.as_view()),
    path('api/v1/elprimos/<int:pk>/', elprimo_views.ElprimoDetailAPIView.as_view()),

    path('api/v1/directors/', directors_views.DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:id>/', directors_views.DirectorDetailAPIView.as_view()),

    path('api/v1/reviews/', reviews_views.RewiewListAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', reviews_views.ReviewDetailAPIView.as_view()),
    path('api/v1/elprimos/reviews/', reviews_views.AverageStarsAPIView.as_view()),

    path('api/v1/users/registration/', el_user.RegistrationAPIView.as_view()),
    path('api/v1/users/authorization/', el_user.AuthorizationAPIView.as_view()),
    path('api/v1/users/confirm/', el_user.ConfirmAPIView.as_view()),
]

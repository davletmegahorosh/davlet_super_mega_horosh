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
from elreiprimo import views, directors_views, reviews_views
from elprimo_user import views as el_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', views.test_api),

    path('api/v1/elprimos/', views.elprimo_list_api_view),
    path('api/v1/elprimos/<int:id>/', views.elprimo_detail_api_view),
    path('api/v1/elprimos/reviews/', reviews_views.average_stars),

    path('api/v1/directors/', directors_views.directors_list_api_view),
    path('api/v1/directors/<int:id>/', directors_views.director_detail_api_view),

    path('api/v1/reviews/', reviews_views.review_list_api_view),
    path('api/v1/reviews/<int:id>/', reviews_views.review_detail_api_view),

    path('api/v1/users/registration/', el_user.registration_view),
    path('api/v1/users/authorization/', el_user.authorization_view),
    path('api/v1/users/confirm/', el_user.confirm_view),
]

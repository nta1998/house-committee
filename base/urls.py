from django.contrib import admin
from django.urls import path, re_path
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    path('test/',views.test),
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('singup/', views.register),
    path('singup/building', views.registerBuilding),
    path('building/', views.BuildingView.as_view()),
    path('building/<id>', views.BuildingView.as_view()),
    path('profile/', views.crudView.as_view()),
    path('profile/All', views.allprofileView.as_view()),
    path('profile/<id>', views.crudView.as_view()),
    path('ads/', views.crudAdsView.as_view()),
    path('ads/<id>', views.crudAdsView.as_view()),
    path('pool/', views.cruPoolView.as_view()),
    path('pool/<id>', views.cruPoolView.as_view()),
    path('adsPay/', views.crudPaymentAdtlView.as_view()),
    path('adsPay/<id>', views.crudPaymentAdtlView.as_view()),
    path('vote/', views.crudVoteView.as_view()),
    path('vote/<id>', views.crudVoteView.as_view()),
    path('chat/', views.ChatVoteView.as_view()),
    path('chat/<id>', views.ChatVoteView.as_view()),
    path('product/', views.ProductsVoteView.as_view()),
    path('product/<id>', views.ProductsVoteView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

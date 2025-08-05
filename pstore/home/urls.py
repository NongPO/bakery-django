from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('bakery/', views.bakery_view, name='bakery'),
    path('drinks/', views.drinks_view, name='drinks'),
    path('special/', views.special_view, name='special'),
    path('tea/', views.tea_view, name='tea'),
    path('cake/', views.cake_view, name='cake'),
    path('recommend/', views.recommend_view, name='recommend'),
]
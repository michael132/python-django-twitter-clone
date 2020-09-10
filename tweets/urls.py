from django.urls import path, re_path
from tweets import views

urlpatterns = [
    path('', views.home_view),
    path('tweets/', views.tweet_list_view),
    path('tweets/<int:tweet_id>', views.tweet_detail_view),
]

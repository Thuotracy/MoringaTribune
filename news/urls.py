from django.urls import re_path
from . import views

urlpatterns= [
    re_path('^$',views.news_today,name = 'newsToday'),
    re_path('^archieves/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    re_path(r'^search/', views.search_results, name='search_results')
    ]


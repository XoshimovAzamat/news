from django.urls import path, include
from .views import *

urlpatterns = [
    path('index/', index),
    path('news_detail/<int:news_id>/', news_detail, name='news_detail'),
    path('search_news/', search_view, name='search_news'),
    path('index/', index, name='index'),
    path('index/', index, name='home'),
    path('categories/<int:category_id>', categories, name='categories'),
    path('update_new/<int:new_id>', update_new, name='update_new'),
    path('new_about/<int:new_id>', new_about, name='new_about'),
    path('add_news/', add_news, name='add_news'),
    path('login', loginPage, name='login'),
    path('del_new/<int:new_id>', del_new, name='del_new'),

]

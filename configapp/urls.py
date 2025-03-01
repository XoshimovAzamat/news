from django.urls import path, include
from .views import *

urlpatterns = [
    path('index/', index),
    path('index/', index, name='index'),
    path('index/', index, name='home'),
    path('categories/<int:category_id>', categories, name='categories'),
    path('update_new/<int:new_id>', update_new, name='update_new'),
    path('new_about/<int:new_id>', new_about, name='new_about'),
    path('add_news/', add_news, name='add_news'),

]

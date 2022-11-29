from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Blog-Home'),
    # the views.home gors to the functio in views and home functio has some html code
    path('about', views.about, name='Blog-About'),  # the views.about gors to the functio in views and about functio
                                                    # has some html code


    # the first parameter with the string: when there is a match with a link it /blog
        # 1. if there is nothing left, i.e. there is nothing following the /blog line 5 is exextued
        # 2. if there is something after /blog and it is about, it shall execute line 6

]

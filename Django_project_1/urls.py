"""Django_project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

import blog_1.urls

urlpatterns = [
    path('admin/', admin.site.urls),  # directs a link with /admin at the end to  the admin page
    path('blog/', include(blog_1.urls)),  # directs to  the file in the 'blog_1" folder with the name urls
    path('', include(blog_1.urls)),  # for the initial homepage to make it the blog home page

    # """
    # the first parameter string in the path  'admin/' or any other is when the link is run and any other thing is like
    # http://localhost:8000/admin or any other in the place of /admin
    #
    # the second one is when the link is input where it is supposed to go
    # for the blog, it goes to the blog_1 folder and sees what is to  do if anything  else is put in following the original
    # like http://localhost:8000/blog/greet
    # """
]

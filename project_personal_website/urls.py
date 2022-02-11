"""project_personal_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app_blog.views import frontpage, post_detail, blog

# to use and store images
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('blog/', blog, name='blog'),
    path('<slug:slug>/', post_detail, name='post_detail'),
]


# where are the files stored?
# django will set up a url pattern for us, so it can serve those media files for us when we tap them in browser url bar. OR request from template
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

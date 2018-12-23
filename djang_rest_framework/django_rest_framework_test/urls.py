# coding: utf-8

from django.conf.urls import url, include
from django.contrib import admin

from blog.urls import router as blog_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # blog.urlsをincludeする
    url(r'^api/', include(blog_router.urls)),
]

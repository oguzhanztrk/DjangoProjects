
from django.contrib import admin
from django.urls import path
from post.views import PostView,my_django_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', PostView.as_view(),name ='post-list'),
    path('dene/',my_django_view),
]

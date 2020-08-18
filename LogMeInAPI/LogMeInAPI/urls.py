
from django.contrib import admin
from django.urls import path,include
from posts import views
urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.userprocess, name='user')
    #path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls'))


]

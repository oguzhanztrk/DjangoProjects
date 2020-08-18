
from django.contrib import admin
from django.urls import path
from Trypincode.views import getpin,home,getAccount,login,listSession,createSession,generateAuthCode
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('pincode/',getpin),
    path('login/',login),
    path('getaccount/', getAccount),
    path('listsession/',listSession),
    path('createsession/',createSession),
    path('generateauthcode/',generateAuthCode),
]

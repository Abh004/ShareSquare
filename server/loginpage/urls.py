# yourapp/urls.py
from django.urls import path
#from .views import login_view
from .views import login,register

urlpatterns = [
    #path('login/', login_view, name='login'),
    path('signup/', register, name='signup'),
    path('login/', login, name='login'),
]

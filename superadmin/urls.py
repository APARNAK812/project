from django.urls import path
from.import views 
app_name='superadmin'



urlpatterns=[
    path('home',views.home),
    path('login',views.login),
    path('index1',views.index1),
    
]
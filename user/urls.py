from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView


app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name= 'user/logout.html'), name='logout'),
    path('register/',views.register, name='register')
]

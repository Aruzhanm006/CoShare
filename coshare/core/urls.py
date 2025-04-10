from django.urls import path
from .views import home_view
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home_view, name='home'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

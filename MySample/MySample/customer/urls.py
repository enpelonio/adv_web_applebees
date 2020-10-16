from django.urls import path
from django.views.generic import View, TemplateView
from . import views 

app_name = 'landing'

urlpatterns = [
    path('index/', views.CustomerIndexView.as_view(), name="index_view"),
    path('registration/', views.CustomerRegistrationView.as_view(), name="registration_view"),
    # path('dashboard/', views.CustomerDashboardView.as_view(), name="index_view"),

]
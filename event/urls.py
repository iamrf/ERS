from django.urls import path
from . import views


app_name = 'event'

urlpatterns = [
    path('', views.EventIndexView.as_view(), name='index'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='detail'),
    path('register/', views.user_register, name='user-register'),
    path('register/completed/', views.completed_register, name='complete'),
]

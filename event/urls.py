from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'event'

urlpatterns = [
    path('', views.EventIndexView.as_view(), name='index'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='detail'),
    path('register/', views.user_register, name='user-register'),
    path('register/completed/', views.completed_register, name='complete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

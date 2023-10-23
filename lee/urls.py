from django.urls import path
from . import views

urlpatterns = [
    path('pro/', views.pro, name='pro'),
    path('kate/', views.kate, name='kate'),
    path('bb/', views.bb, name='bb'),
]
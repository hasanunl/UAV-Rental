from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uavs/', views.UavListView.as_view(), name='uavs'),
    path('uav/<int:pk>', views.UavDetailView.as_view(), name='uav-detail'),
]


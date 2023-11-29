from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uavs/', views.UavListView.as_view(), name='uavs'),
    path('uav/<int:pk>', views.UavDetailView.as_view(), name='uav-detail'),
]

urlpatterns += [
    path('myuavs/', views.RentedUavsByUserListView.as_view(), name='my-rented'),
]

urlpatterns += [
    path('uav/<uuid:pk>/renew/', views.renew_uav_member, name='renew-uav-member'),
]

urlpatterns += [
    path('uavinstance/create/', views.UavInstanceCreate.as_view(),
         name='uavinstance-create'),
    path('uavinstance/<uuid:pk>/update/',
         views.UavInstanceUpdate.as_view(), name='uavinstance-update'),
    path('uavinstance/<uuid:pk>/delete/',
         views.UavInstanceDelete.as_view(), name='uavinstance-delete'),
]
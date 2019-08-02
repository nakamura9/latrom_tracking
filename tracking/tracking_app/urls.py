from django.urls import path
from . import views 

reports = [
    path('reports/moving-overview/', views.MovingOverViewReport.as_view(), 
        name='moving-overview'),
]
urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('business/home/', views.BusinessHomePage.as_view(), 
        name='business-home'),
    path('monitor/home/', views.MonitorHome.as_view(), 
        name='monitor-home'),
    path('create-customer/', views.CustomerCreateView.as_view(), 
        name='create-customer'),
    path('update-customer/<int:pk>', views.CustomerUpdateView.as_view(), 
        name='update-customer'),
    path('customer/detail/<int:pk>', views.CustomerDetailView.as_view(), 
        name='customer-detail'),
    path('create-device/', views.DeviceCreateView.as_view(), 
        name='create-device'),
    path('customer/<int:pk>/devices/', views.DeviceListView.as_view(), 
        name='customer-devices'),
    path('customer/<int:pk>/sub-accounts/', views.CustomerSubaccountListView.as_view(), 
        name='customer-sub-accounts'),
    path('update-device/<int:pk>', views.DeviceUpdateView.as_view(), 
        name='update-device'),
    path('devices/', views.DevicesListView.as_view(), 
        name='devices'),
    path('statistics/', views.StatisticsView.as_view(), 
        name='statistics'),

] + reports
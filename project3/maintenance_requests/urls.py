from django.urls import path
from . import views

# URLConf module
urlpatterns = [
    path('', views.view_requests, name="index"),
    path('new_request', views.new_request, name="new_request"),
    path('tenants', views.view_tenants, name="tenants"),
    path('new_tenant', views.new_tenant, name="new_tenant"),
    path('delete_tenant/<str:pk>/', views.delete_tenant, name="delete_tenant"),
    path('edit_tenant/<str:pk>/', views.edit_tenant, name="edit_tenant"),
    path('maintenance', views.maintenance_view, name="maintenance"),
    path('change_request_status/<str:pk>/', views.change_request_status, name="change_request_status")
]
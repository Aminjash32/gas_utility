# gas_utility_service/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/customers/', include('customer.urls')),
    path('api/service_requests/', include('service_request.urls')),
    path('api/support/', include('support.urls')),
]

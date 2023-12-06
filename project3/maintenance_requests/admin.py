from django.contrib import admin


from .models import Maintenance_Request
admin.site.register(Maintenance_Request)

from .models import Tenant
admin.site.register(Tenant)

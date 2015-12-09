from django.contrib import admin

from .models import CannedResponse


#-----------------------------------------------------------------------------
class CannedResponseAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'request_method', 'request_path', 'response_status_code', )
    list_filter = ('active', 'request_method', 'response_status_code', )
    list_editable = ('active', )
    ordering = ('request_path', '-active', )


admin.site.register(CannedResponse, CannedResponseAdmin)


# [EOF] admin.py

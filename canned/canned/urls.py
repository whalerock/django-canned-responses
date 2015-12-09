from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^.*$', 'canned.canned_responses.views.canned_response_view', name='canned-response-view'),
]


# [EOF] urls.py

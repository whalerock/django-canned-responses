import time

from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

from .models import CannedResponse


#-----------------------------------------------------------------------------
@csrf_exempt
def canned_response_view(request):
    '''
    Simple view to return a canned response for the incoming request. Find the
    first active CannedResponse instance for the request's method and path,
    then simply return its get_http_response(). If no CannedResponse instance
    is found meeting the requirements of the request, raise an Http404.
    '''
    cr = CannedResponse.objects.filter(
        active=True,
        request_method=request.method,
        request_path=request.path,
    ).first()
    if not cr:
        raise Http404("Path not found.")
    
    if cr.response_sleep_time:
        time.sleep(cr.response_sleep_time)
    
    return cr.get_http_response()


# [EOF] views.py

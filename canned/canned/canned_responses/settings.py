from django.conf import settings


default_req_method_choices = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PATCH', 'PATCH'),
    )
REQUEST_METHOD_CHOICES = getattr(settings, 'REQUEST_METHOD_CHOICES', default_req_method_choices)


default_response_content_type_choices = (
    ('application/json', 'JSON'),
    ('text/html', 'HTML'),
)
RESPONSE_CONTENT_TYPE_CHOICES = getattr(settings, 'RESPONSE_CONTENT_TYPE_CHOICES', default_response_content_type_choices)


# [EOF] settings.py

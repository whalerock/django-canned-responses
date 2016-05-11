from django.db import models
from django.http import HttpResponse

from settings import REQUEST_METHOD_CHOICES
from settings import RESPONSE_CONTENT_TYPE_CHOICES


# -----------------------------------------------------------------------------
class CannedResponse(models.Model):
    '''
    Model to store canned responses for different request methods/paths.
    '''
    name = models.CharField(max_length=1024)
    active = models.BooleanField(default=True, db_index=True)
    request_method = models.CharField(max_length=32, choices=REQUEST_METHOD_CHOICES, db_index=True)
    request_path = models.CharField(max_length=1024, db_index=True)
    response_status_code = models.IntegerField(default=200)
    response_sleep_time = models.IntegerField(default=0)
    response_content_type = models.CharField(max_length=64, choices=RESPONSE_CONTENT_TYPE_CHOICES)
    response_headers = models.TextField(
        default="",
        blank=True,
        help_text="Enter the headers one on each line 'Location: http://google.com/'")
    response_payload = models.TextField()

    class Meta:
        verbose_name = 'Canned Response'
        verbose_name_plural = 'Canned Responses'

    def __unicode__(self):
        return unicode("%s - %s (%s)" % (self.request_method, self.request_path, self.name))

    def save(self, *args, **kwargs):
        if self.active:
            # convenience - deactivate others with same request_method and request_path
            self._deactivate_others_of_same_method_path()
        super(CannedResponse, self).save(*args, **kwargs)

    def get_http_response(self):
        response = HttpResponse(
            content_type=self.response_content_type,
            status=self.response_status_code,
            content=self.response_payload
        )
        if self.response_headers:
            for line in self.response_headers.split('\n'):
                if ":" in line:
                    key, value = line.split(":", 1)
                    response[key] = value.strip()
        return response

    def _deactivate_others_of_same_method_path(self):
            self.__class__.objects.filter(
                request_method=self.request_method,
                request_path=self.request_path,
            ).update(active=False)


# [EOF] models.py

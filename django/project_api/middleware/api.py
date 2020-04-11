from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest
import json
import logging

logger = logging.getLogger(__name__)


class ApiMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        ApiMiddleware.process_response(request, response)

        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Exception):
            pass

    @classmethod
    def process_response(cls, request, response, form):
        if response.status_code == 200:
            pass

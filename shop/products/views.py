
import logging

from django.conf import settings
from django.http import HttpResponse
logger = logging.getLogger(__name__)


def index(request):
    logger.info(request.GET)
    if request.GET.get("param"):
        logger.info(f"My custom var = {settings.MY_VARIABLE}")
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Shop index view")


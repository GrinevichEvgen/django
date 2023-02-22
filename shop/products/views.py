
import logging
from django.http import HttpResponse
logger = logging.getLogger(__name__)


def index(request):
    logger.info(request.GET, request.POST)
    if request.GET.get("param"):
        logger.error(f"My param = {request.GET.get('param')}")
    return HttpResponse("Shop index view")

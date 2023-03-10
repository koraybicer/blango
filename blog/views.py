from django.shortcuts import render
import logging
from models import Post


logger = logging.getLogger(__name__)
# Create your views here.

def index(request):
  posts = Post.objects.all()
  logger.debug("Got %d posts", len(posts))


def post_detail(request):
  if request.POST:
    
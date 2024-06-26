from . import models


def get_all_videos():
  return models.Video.objects.all()
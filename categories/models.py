from django.db import models
from commonmodel.models import CommonModel

class Category(CommonModel):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

  
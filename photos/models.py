from django.db import models
from commonmodel.models import CommonModel

class Photo(CommonModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title

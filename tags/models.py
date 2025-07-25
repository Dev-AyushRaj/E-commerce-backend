from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # what tag applied to what object
    tag = models.ForeignKey(Tag, on_delete= models.CASCADE)
    # Type (product,video, artical)
    # ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null= True)
    object_id = models.PositiveIntegerField(null= True)
    content_object = GenericForeignKey()


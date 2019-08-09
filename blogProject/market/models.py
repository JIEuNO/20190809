from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Market(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='upload2/', default="/")
    price=models.IntegerField()
    num=models.IntegerField()
    category=models.CharField(max_length=200)
    description=RichTextUploadingField(blank=True, null=True)
    sentence=models.CharField(max_length=200)

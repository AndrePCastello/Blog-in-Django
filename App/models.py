from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Posts(models.Model):

    option_types = (
        ('F', 'filosofia'),
        ('T','tecnologia'),
        ('R', 'Regras'),
    )

    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    content = RichTextUploadingField(default='')
    date_creat = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=20, choices=option_types)
    thumb_image = models.ImageField(upload_to='App/static/thumb')
    

    def __str__(self):
        return self.title
    





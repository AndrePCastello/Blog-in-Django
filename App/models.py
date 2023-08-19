from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):

    option_types = (
        ('Filosofia', 'filosofia'),
        ('Tecnologia','tecnologia'),
        ('Regras', 'Regras'),
    )

    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    content = RichTextUploadingField(default='')
    date_creat = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=20, choices=option_types)
    

    def __str__(self):
        return self.title
    





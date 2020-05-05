import uuid
from django.db import models
from django.urls import reverse


# Create your models here.

class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.IntegerField()
    page_length = models.IntegerField()
    assigned_class = models.CharField(max_length=75, blank=True)
    subject = models.CharField(max_length=75)
    cover = models.ImageField(upload_to='covers/', blank=True)
  
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])
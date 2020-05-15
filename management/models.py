from django.db import models

# Create your models here.
import uuid
from datetime import date
from django.urls import reverse
from users.models import CustomUser
from books.models import Author, Book, Class, BookInstance
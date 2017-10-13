from django.db import models
from django.conf import settings
# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    ebook = models.FileField(upload_to='ebook')
    def __str__(self):
        return self.book_name

class PurchaseCase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    
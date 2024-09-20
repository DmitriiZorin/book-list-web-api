from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(null=False, max_length=200)
    author = models.CharField(null=False, max_length=100)
    date_published = models.DateField(null=False)

    def __str__(self):
        return '%s (%s), %s' % self.name, self.author, self.date_published

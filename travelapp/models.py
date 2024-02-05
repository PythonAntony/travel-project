from django.db import models

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

class features(models.Model):
    name = models.CharField(max_length=250)
    img1 = models.ImageField(upload_to='pics')
    img2 = models.FileField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name
from django.db import models

class SiteSetting(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos/')
    # any other fields…

    def __str__(self):
        return self.title


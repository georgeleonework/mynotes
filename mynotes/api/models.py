from django.db import models

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True) #every time the save method is run the updated field is timestamped
    created = models.DateTimeField(auto_now_add=True) #only takes the timestamp one time

    def __str__(self):
        return self.body[0:50]
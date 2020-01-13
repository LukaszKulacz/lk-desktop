from django.db import models

# Create your models here.
class ToDo(models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
    
    def _str_(self):
        return self.text
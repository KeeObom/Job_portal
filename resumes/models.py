from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='cv/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
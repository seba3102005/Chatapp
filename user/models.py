from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.

class ChatRoom(models.Model):
    owner = models.ForeignKey(user,on_delete=models.CASCADE)
    client = models.ManyToManyField(user,related_name='my_chatrooms')
    name = models.CharField(max_length=100,unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
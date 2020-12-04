from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200) #display 200 characters only
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    #prints title in our admin panel
    def __str__(self):
        return self.title
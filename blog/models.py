from django.db import models
# Create your models here.

from django.conf import settings
from django.utils import timezone

class Post(models.Model):#models.Modelはポストがdjangoモデルだという意味。djangoが、これはデータベースに保存するものだとわかるようにしている。
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)#link to the other model
    title = models.CharField(max_length = 200)#limited text field
    text = models.TextField()#unlimited text field
    created_data = models.DateTimeField(default = timezone.now)
    published_data = models.DateTimeField(blank=True,null=True)
    
    def publish(self):#method to publish blog
        self.published_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title











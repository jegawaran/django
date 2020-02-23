from django.db import models

# Create your models here.

class NewTopic(models.Model):
    topic_name = models.CharField(max_length=264,unique=True)
    
    def __str__(self):
        return self.topic_name
    
class NewWebpage(models.Model):
    new_topic = models.ForeignKey(NewTopic, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=265)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name
    
    
    
    

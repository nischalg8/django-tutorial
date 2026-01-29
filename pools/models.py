import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to="questions/", blank=True, null=True)
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Choice(models.Model):
    CHOICE_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
    ]
    question = models.ForeignKey(Questions, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    type = models.CharField(max_length=2, choices = CHOICE_TYPE_CHOICE, default='ML')
    
    def __str__(self):
        return self.choice_text
    
    

from django.db import models
from datetime import *
from home.models import *
# Create your models here.

class daily_attendance(models.Model):
    student = models.CharField(max_length = 500)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, default=0)   #models.IntegerField()
    faculty = models.IntegerField()
    attendance_date = models.DateField('date published', default=date.today)
    update_date = models.DateTimeField('date published', default=datetime.now)

class allmessages(models.Model):
    message_text = models.TextField()
    m_from = models.IntegerField()
    m_to = models.CharField(max_length = 500)
    status = models.IntegerField(default=0)
    creation_date = models.DateTimeField('date published', default=datetime.now)
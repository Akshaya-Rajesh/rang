from django.db import models

# Create your models here.
class Participant(models.Model):
    cat_list = {
        ('school','school'),
        ('campus','campus'),
        ('senior','senior')
    }
    district_list = {
        ('alappuzha','Alappuzha'),
        ('ernakulam','Ernakulam'),
        ('idukki','Idukki'),
        ('kannur','Kannur'),
        ('kasaragod','Kasaragod'),
        ('kollam','Kollam'),
        ('kottayam','Kottayam'),
        ('kozhikode','Kozhikode'),
        ('malappuram','Malappuram'),
        ('palakkad','Palakkad'),
        ('pathanamthitta','Pathanamthitta'),
        ('thiruvananthapuram','Thiruvananthapuram'),
        ('thrissur','Thrissur'),
        ('wayanad','Wayanad'),
    }
    name = models.CharField(max_length=256)
    district = models.CharField(max_length=20,choices=district_list)
    category = models.CharField(max_length=10,choices=cat_list)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Paricipation(models.Model):
    participant = models.ForeignKey(Participant , on_delete=models.PROTECT)
    event = models.ForeignKey(Event , on_delete=models.PROTECT)
    score = models.IntegerField()
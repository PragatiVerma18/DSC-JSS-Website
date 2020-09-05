from django.db import models

# Create your models here.

DESIGNATION_CHOICES = ( 
    ("Lead", "Lead"), 
    ("Developer", "Developer"), 
    ("Designer", "Designer"), 
    ("Programmer", "Programmer"), 
    ("Management", "Management"), 
) 

YEAR_CHOICES = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
)

EVENT_SCHEDULE = (
    ("Upcoming","Upcoming"),
    ("Past","Past"),
)

class Members(models.Model):
    name=models.CharField(max_length=30)
    image=models.FileField(upload_to='members/')
    designation=models.CharField(choices=DESIGNATION_CHOICES,max_length=20)
    github=models.URLField(blank=False)
    linkedin=models.URLField(blank=False)
    dribbleorbehance=models.URLField(blank=True)
    year=models.CharField(choices=YEAR_CHOICES, max_length=5)

    def __str__(self):
        return self.name


class Projects(models.Model):
    name=models.CharField(max_length=50)
    image=models.FileField(upload_to='projects/')
    link=models.URLField(blank=True)
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Event(models.Model):
    title=models.CharField(max_length=50)
    startdate=models.DateField()
    enddate=models.DateField()
    starttime=models.TimeField(auto_now=False, auto_now_add=False)
    endtime=models.TimeField(auto_now=False, auto_now_add=False)
    poster=models.FileField(upload_to='events/')
    schedule=models.CharField(choices=EVENT_SCHEDULE, max_length=20)

    def __str__(self):
        return str(self.pk)+" "+self.title


class Registration(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,limit_choices_to={'schedule': 'Upcoming'})
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phonenumber=models.IntegerField()


    def __str__(self):
        return self.name
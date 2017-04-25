from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Job(models.Model):

    user = models.ForeignKey(User, related_name='Use', on_delete=models.CASCADE) 
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    catagory = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE)
    salary = models.IntegerField(blank=True)
    company_name = models.CharField(max_length=300)
    company_description = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    last_date = models.DateField()
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Applicant(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.name.id
    
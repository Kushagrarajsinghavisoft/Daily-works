from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional data for user model
    COURSE_CHOICES = (
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('MERN', 'MERN'),
    )
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return str(self.user)

class Todo(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)
    
    COURSE_CHOICES = (
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('MERN', 'MERN'),
    )
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)

    def __str__(self):
        return f"{self.sno} -> {self.title}"


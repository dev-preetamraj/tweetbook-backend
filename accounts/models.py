from django.db import models
from django.contrib.auth.models import User

def upload_to_profile_path(instance, filename):
    return f'users/profile/{instance.user.username}_{filename}'

def upload_to_cover_path(instance, filename):
    return f'users/cover/{instance.user.username}_{filename}'

class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    RELATIONSHIP_STATUS_CHOICES = (
        ('Ma', 'Married'),
        ('Si', 'Single'),
        ('Co', 'Committed'),
        ('Di', 'Divorced'),
        ('En', 'Engaged'),
        ('Se', 'Separated'),
        ('Oa', 'Open For All')
    )

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    profile_picture = models.ImageField(upload_to=upload_to_profile_path, default='users/profile.png')
    cover_picture = models.ImageField(upload_to=upload_to_cover_path, default='users/cover.jpg')
    bio = models.CharField(max_length=255, null=True, blank=True)
    relationship_status = models.CharField(max_length=2, choices=RELATIONSHIP_STATUS_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
    
class Friendship(models.Model):
    STATUS_CHOICES = (
        ('A', 'Accepted'),
        ('P', 'Pending'),
        ('R', 'Restricted'),
        ('B', 'Blocked')
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.friend.username}: Friendship'
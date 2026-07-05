from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        default="profile_pictures/default.png"
    )

    cover_photo = models.ImageField(
        upload_to="cover_photos/",
        blank=True,
        null=True
    )

    bio = models.TextField(blank=True)

    about = models.TextField(blank=True)

    location = models.CharField(
        max_length=100,
        blank=True
    )

    education = models.CharField(
        max_length=200,
        blank=True
    )

    profession = models.CharField(
        max_length=150,
        blank=True
    )

    website = models.URLField(blank=True)

    github = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    twitter = models.URLField(blank=True)

    skills = models.TextField(
        blank=True,
        help_text="Comma separated skills"
    )

    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Follow(models.Model):
    follower = models.ForeignKey(
        User,
        related_name='following_users',
        on_delete=models.CASCADE
    )

    following = models.ForeignKey(
        User,
        related_name='follower_users',
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower} follows {self.following}"

    
class Badge(models.Model):

    title = models.CharField(max_length=100)

    icon = models.CharField(max_length=50)

    color = models.CharField(
        max_length=30,
        default="primary"
    )

    def __str__(self):
        return self.title


class UserBadge(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    badge = models.ForeignKey(
        Badge,
        on_delete=models.CASCADE
    )
    


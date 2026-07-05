from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Event(models.Model):

    CATEGORY_CHOICES = [
        ("Workshop", "Workshop"),
        ("Seminar", "Seminar"),
        ("Hackathon", "Hackathon"),
        ("Meetup", "Meetup"),
        ("Webinar", "Webinar"),
        ("Competition", "Competition"),
        ("Conference", "Conference"),
        ("Other", "Other"),
    ]

    TYPE_CHOICES = [
        ("Online", "Online"),
        ("Offline", "Offline"),
        ("Hybrid", "Hybrid"),
    ]

    STATUS_CHOICES = [
        ("Upcoming", "Upcoming"),
        ("Ongoing", "Ongoing"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    organizer = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="organized_events",
    null=True,
    blank=True
)

    title = models.CharField(max_length=200)

    description = models.TextField()

    banner = models.ImageField(
        upload_to="event_banners/",
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Workshop"
    )

    event_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default="Offline"
    )

    address = models.CharField(
        max_length=300,
        default="Address not specified",
        blank=True
    )

    google_map_link = models.URLField(
        blank=True,
        default=""
    )

    start_datetime = models.DateTimeField(
        default=timezone.now
    )

    end_datetime = models.DateTimeField(
        default=timezone.now
    )

    registration_deadline = models.DateTimeField(
        default=timezone.now
    )

    capacity = models.PositiveIntegerField(
        default=100
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Upcoming"
    )

    is_public = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


class EventJoin(models.Model):

    RSVP_CHOICES = [
        ("Going", "Going"),
        ("Interested", "Interested"),
        ("Not Going", "Not Going"),
    ]

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="attendees"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=RSVP_CHOICES,
        default="Interested"
    )

    checked_in = models.BooleanField(
        default=False
    )

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ("event", "user")


class Notification(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    message = models.CharField(
        max_length=200
    )

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.message


class EventGallery(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="gallery"
    )

    image = models.ImageField(
        upload_to="event_gallery/"
    )


class EventMessage(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["created_at"]


class EventCheckIn(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    attendee = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    qr_token = models.CharField(
        max_length=255,
        unique=True
    )

    checked_in = models.BooleanField(
        default=False
    )

    checked_in_at = models.DateTimeField(
        null=True,
        blank=True
    )
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ("UNASSIGNED", "Unassigned"),
        ("IN_PROGRESS", "In Progress"),
        ("DONE", "Done"),
        ("ARCHIVED", "Archived"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False, default="Add some description")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="UNASSIGNED",
        db_comment="Can be UNASSIGNED, IN_PROGRESS, DONE, or ARCIVED",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        User, related_name="created_tasks", on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        User, related_name="owned_tasks", on_delete=models.SET_NULL, null=True
    )


class Meta:
    db_table_comment = "Holds information about tasks"
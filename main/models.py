from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):

    project_name = models.CharField(verbose_name = "Project Name", max_length = 250, null = False) #

class Task(models.Model):
 
    STATUS_CHOICES = [
        ("pending", "Pending"), #
        ("in_progress", "In Progress"), #
        ("done", "Done") #
    ]

    tittle = models.CharField(verbose_name = "Tittle", max_length = 250, null = False) #
    description = models.CharField(verbose_name = "Description", max_length = 250, null = False) #
    status = models.CharField(verbose_name = "Status", choices = STATUS_CHOICES, max_length = 25, default = "pending") #
    deadline = models.DateTimeField(verbose_name = "Deadline", null = False) #
    project = models.ForeignKey(Project, verbose_name = "Project", on_delete = models.CASCADE) #
    assigned_to = models.ForeignKey(User, verbose_name = "Assigned To", on_delete = models.SET_NULL, null = True, blank = True)

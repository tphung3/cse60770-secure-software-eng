from django.db import models


# The status for a task
TASK_STATUS_CHOICES = [
    ('C', 'Completed'),
    ('I', 'In progress'),
    ('N', 'Not started yet'),
]

# Specifies the Task table in the database
class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    status =  models.CharField(max_length=1, choices=TASK_STATUS_CHOICES) 
    def __str__(self):
    	return f"Task #{self.id}: {self.title}" 

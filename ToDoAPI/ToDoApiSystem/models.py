from django.db import models


class ToDo(models.Model):
    description = models.TextField(max_length=300)
    duedate = models.DateTimeField()
    status = models.CharField(max_length=20)

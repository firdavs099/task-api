from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=250)
    task_desc = models.TextField(blank=True)
    task_pub_date = models.DateTimeField(auto_now_add=True)
    progress = models.ForeignKey('TaskProgress', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.task_name


class TaskProgress(models.Model):
    prog_type = models.CharField(max_length=150)

    def __str__(self):
        return self.prog_type

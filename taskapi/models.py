from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=150)
    task_desc = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.task_name

class Category(models.Model):
    cat_name = models.CharField(max_length=150, db_index=True) 

    def __str__(self):
        return self.cat_name
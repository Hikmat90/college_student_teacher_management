from django.db import models
from user.models import Student
# Create your models here.
class content(models.Model):
    created_by = models.ForeignKey(Student, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    content = models.CharField(max_length = 400)
    
    def __str__(self):
        return self.created_by
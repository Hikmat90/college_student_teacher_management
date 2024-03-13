from django.db import models
from django.core.validators import MinLengthValidator

AVAILABLE_ID = [
    ('1111', '1111'),
    ('2222', '2222'),
    ('3333', '3333'),
    ('4444', '4444'),
]

# Correctly define faculty choices
FACULTY_CHOICES = [
    ('BIT', 'Bachelor of Information Technology'),
    ('BTECH', 'Bachelor of Technology'),
    ('CIVIL', 'Civil Engineering'),
    ('BBA', 'Bachelor of Business Administration'),
]

class Student(models.Model):
    username = models.CharField(max_length=50)
    faculty = models.CharField(max_length=20, choices=FACULTY_CHOICES)
    roll_no = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128, validators=[MinLengthValidator(limit_value=8)])  # Password field with min_length 8
    
    def __str__(self):
        return self.username

class Teacher(models.Model):
    username = models.CharField(max_length=50)
    department = models.CharField(max_length=10, choices=FACULTY_CHOICES)
    id_no = models.CharField(max_length=4, choices=AVAILABLE_ID)  # Added max_length
    password = models.CharField(max_length=128, validators=[MinLengthValidator(limit_value=8)])  # Password field with min_length 8
    
    def __str__(self):
        return self.username  # Corrected from self.name to self.username

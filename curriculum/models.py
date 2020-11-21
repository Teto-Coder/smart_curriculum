from django.db import models

class UserData(models.Model):
    userName =  models.CharField(max_length=50, default="", editable=False)
    userEmail = models.CharField(max_length=50, default="", editable=False)
    userPassword = models.CharField(max_length=50, default="", editable=False)
    userSchool = models.CharField(max_length=50, default="", editable=False)
    userMajor = models.CharField(max_length=50, default="", editable=False)
    isTeacher = models.BooleanField(max_length=50, default=False, editable=False)
    courses =  models.CharField(max_length=500, default="", editable=False)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "UserData"

class AllCourse(models.Model):
    courseId =  models.CharField(max_length=50, default="", editable=False)
    courseName =  models.CharField(max_length=50, default="", editable=False)
    info =  models.CharField(max_length=500, default="", editable=False)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "AllCourse"

class QA(models.Model):
    courseId =  models.CharField(max_length=50, default="", editable=False)
    Question = models.CharField(max_length=500, default="", editable=False)
    Answer = models.CharField(max_length=500, default="", editable=False)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "QA"

class Exam(models.Model):
    courseId =  models.CharField(max_length=50, default="", editable=False)
    examName =  models.CharField(max_length=50, default="", editable=False)
    time =  models.CharField(max_length=50, default="", editable=False)
    info = models.CharField(max_length=500, default="", editable=False)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "Exam"

class HomeWork(models.Model):
    courseId =  models.CharField(max_length=50, default="", editable=False)
    HWName =  models.CharField(max_length=50, default="", editable=False)
    time =  models.CharField(max_length=50, default="", editable=False)
    info = models.CharField(max_length=500, default="", editable=False)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "HomeWork"
        
class Announcement(models.Model):
    courseId =  models.CharField(max_length=50, default="", editable=False)
    AnnouncementName =  models.CharField(max_length=50, default="", editable=False)
    info = models.CharField(max_length=500, default="", editable=False)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "Announcement"
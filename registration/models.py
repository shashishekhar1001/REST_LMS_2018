from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import os
from django.conf import settings
from djangotoolbox.fields import ListField


class Custom_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    REGISTRATION_CHOICES = (
        ('Learner', 'Learner'),
        ('Trainer', 'Trainer'),
        ('Vendor', 'Vendor'),
        ('Client', 'Client'),
        ('Job Seeker', 'Job Seeker'),
    )
    primary_registration_type = models.CharField(max_length=15, choices=REGISTRATION_CHOICES)    
    secondary_registration_type = models.CharField(max_length=15, choices=REGISTRATION_CHOICES, blank=True)    
    tertiary_registration_type = models.CharField(max_length=15, choices=REGISTRATION_CHOICES, blank=True)    
    quaternary_registration_type = models.CharField(max_length=15, choices=REGISTRATION_CHOICES, blank=True)   
    
    def __str__(self):
        return self.user.email

class Trainer_Model(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile_pics/%Y/%m/%d/', blank=True)
    courses_tutoring = models.TextField()
    describe_yourself = models.TextField()
    linked_in_url = models.URLField()
    skills = models.TextField(blank=True)
    cv = models.FileField(upload_to='cvs/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.user.user.email


class Course(models.Model):
    thumbnail = models.ImageField(upload_to='Course_Thumbnails/%Y/%m/%d/', blank=True)
    course_by = models.ForeignKey(Trainer_Model)
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    prerequisite = models.TextField()
    requirements = models.TextField()
    rating = models.FloatField(default=0)
    no_of_ratings = models.FloatField(default=0)
    author = models.CharField(max_length=200, blank=True, default=None, null=True)

    def get_absolute_url(self):
        return reverse('edit_course', kwargs={'course_id': self.id})

    def save(self, *args, **kwargs):
        if getattr(self, 'author_changed', True):
            self.author = self.course_by.user.user.get_full_name()
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.course_name + "  --By " + self.course_by.user.user.get_full_name()

    class Meta:
        permissions = (
            ('access_course', 'Access Course'),
        )
    


def content_videofile_name(instance, filename):
    return '/'.join(['Videos', instance.part_of.course_by.user.user.get_full_name(), instance.part_of.course_name, filename])


def content_pptfile_name(instance, filename):
    return '/'.join(['PPT', instance.part_of.course_by.user.user.get_full_name(), instance.part_of.course_name, filename])

def content_assignmentfile_name(instance, filename):
    return '/'.join(['Assignments', instance.part_of.course_by.user.user.get_full_name(), instance.part_of.course_name, filename])

def content_referencefile_name(instance, filename):
    return '/'.join(['References', instance.part_of.course_by.user.user.get_full_name(), instance.part_of.course_name, filename])


class Course_Module(models.Model):
    part_of = models.ForeignKey(Course, related_name='modules')
    name = models.CharField(max_length=200)

    video = models.FileField(   
        upload_to=content_videofile_name,
        blank=True,
        null=True
    )
    
    Presentation = models.FileField(   
        upload_to=content_pptfile_name,        
        blank=True,
        null=True
    )

    Assignment = models.FileField(   
        upload_to=content_assignmentfile_name,        
        blank=True,
        null=True
    )

    Refernce = models.FileField(   
        upload_to=content_referencefile_name,        
        blank=True,
        null=True
    )

    topics = models.TextField(blank=True, null=True)

    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    part_of = models.ForeignKey(Course_Module)
    topic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_name


class Answer_Options(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Answer Option"
        verbose_name_plural = "Answer Options"


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=200)
    module_referred = models.ForeignKey(Course_Module, related_name="quiz")

    def __str__(self):
        return self.quiz_name

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizes"



class Quiz_Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, default=None, null=True, related_name='questions')
    q_type = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    possible_answers = models.ManyToManyField(Answer_Options)
    selected = models.ForeignKey(Answer_Options, related_name="selected", default=None, on_delete=models.CASCADE, blank=True, null=True)
    correct = models.ForeignKey(Answer_Options, related_name="correct", default=None, on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Quiz Question"
        verbose_name_plural = "Quiz Questions"


class Learner_Model(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/%Y/%m/%d/', blank=True, null=True)
    courses_learning = models.TextField()
    courses_subscribed = models.ManyToManyField(Course, blank=True, null=True)

    def __str__(self):
        return self.user.user.email



class LearnerQnA(models.Model):
    quiz_question = models.ForeignKey(Quiz_Question)
    learner = models.ForeignKey(Learner_Model)
    chosen_option = models.ForeignKey(Answer_Options, related_name="chosen_option", default=None, blank=True, null=True)


class Subscription(models.Model):
    learner = models.ForeignKey(Learner_Model)
    course = models.ForeignKey(Course)
    start_date = models.DateTimeField(auto_now_add = True, auto_now = False)
    end_date = models.DateTimeField()
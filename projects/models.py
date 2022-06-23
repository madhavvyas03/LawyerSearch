from multiprocessing.sharedctypes import Value
from statistics import mode
from django.db import models
import uuid

class Lawyer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    featured_image=models.ImageField(null=True,blank=True)
    practice_area=models.ManyToManyField('Tag',blank=True)
    languages=models.ManyToManyField('Language',blank=True)
    court=models.ManyToManyField('Court',blank=True)
    total_users=models.IntegerField(default=0,null=True,blank=True)
    rating=models.IntegerField(default=0,null=True,blank=True)
    location=models.CharField(max_length=200)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    experience=models.IntegerField(default=0,null=True,blank=True)
    
    def __str__(self):
        return self.title 

class Review(models.Model):
    vote_type=(
        ("up","Up Vote "),
        ("down","Down Vote "),
    )
    project = models.ForeignKey(Lawyer,on_delete=models.CASCADE)
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200,choices=vote_type)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.value 

class Tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.name

class Language(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.name

class Court(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.name
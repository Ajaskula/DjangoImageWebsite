from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=200)


class SVGImage(models.Model):
    image_name = models.CharField(max_length=200, default="1")
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    viewbox = models.CharField(max_length=50) # obszar widzenia obrazka
    version = models.CharField(max_length=10) # wersja svg
    xmlns = models.URLField()
    users = models.ManyToManyField(User)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now())
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.image_name

    def add_rectangle(self, x, y, width, height, fill):
        return self.rectangles.create(x=x, y=y, width=width, height=height, fill=fill)
    
    def del_rectangle(self, rectangle_id):
        rectangle = get_object_or_404(Rectangle, pk=rectangle_id)
        rectangle.delete()

    def add_user(self, user):
        self.users.add(user)
        self.save()
        
    def add_tag(self, tag):
        self.tags.add(tag)
        self.save()

class Rectangle(models.Model):
    svg_image = models.ForeignKey(SVGImage, on_delete=models.CASCADE, related_name='rectangles')
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField() 
    fill = models.CharField(max_length=20) # wypełnienie

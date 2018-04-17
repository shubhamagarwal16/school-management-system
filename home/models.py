from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
# Create your models here.

class Sections(models.Model):
    name = models.CharField(max_length = 200, unique=True)
    creation_date = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.name

class Facultys(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 100, unique=True)
    password = models.CharField(max_length = 200)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, default=0)
    creation_date = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        # dat = self.name + self.email + self.section +" " +self.section
        return self.name +" " +self.email

class Students(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.CharField(max_length=200)
    email = models.EmailField(max_length = 100)
    phone = models.IntegerField(default = 1)
    mother_name = models.CharField(max_length=201)
    gender = models.IntegerField()
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, default=0)
    slug = models.SlugField(max_length=251, default="1")
    creation_date = models.DateTimeField('date published', default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Students, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

from django.db import models

from users.models import Profile


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 blank=True, null=True, related_name='cars')
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                               blank=True, null=True, related_name='owner_cars')
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    engine = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='cars', default='car.png')
    release_auto = models.DateTimeField()
    color = models.CharField(max_length=50)
    transmission = models.BooleanField(default=True)
    rul = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    seen_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

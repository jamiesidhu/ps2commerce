from turtle import title
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing (models.Model):
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 512)
    start_bid = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=64, blank=True)
    img_url = models.URLField(max_length=256, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return str(self.title)

class Bid ():
    pass

class Comment ():
    pass

class Watchlist(models.Model):
    the_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    the_listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    #unique_together = ["the_user", "listing"]
    
    def __str__(self):
        return f"{self.listing} is on {self.the_user}'s watchlist"

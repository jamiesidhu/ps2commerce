from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Watchlist, Comment, Bid

# My additions
from django.forms import ModelForm
from . import util
from django.contrib.auth.decorators import login_required


def index(request):
    listings = util.get_listings()
    return render(request, "auctions/index.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

class newlistform (ModelForm):
    def __init__(self, *args, **kwargs):
        super(newlistform, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Listing
        fields = ["title", "description", "start_bid", "category", "img_url"]

@login_required(login_url="login")
def listitem(request):
    if request.method == "GET":
        form = newlistform()
        return render(request, "auctions/list.html", {
            "form": form
        })
    elif request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        start_bid = request.POST["start_bid"]
        category = request.POST["category"]
        img_url = request.POST["img_url"]
        addlist = Listing(title = title, description = description, start_bid = start_bid, category = category, img_url=img_url, seller = User.objects.get(pk=request.user.id))
        addlist.save()
        # change redirect to listing later
        return HttpResponseRedirect(reverse("index"))


def listing(request, title):

    # Watchlist
    if request.user.is_authenticated:
        watchlist_item = Watchlist.objects.filter(
                the_listing = Listing.objects.get(title=title),
                the_user = User.objects.get(id=request.user.id)
        ).first()

        if watchlist_item is not None:
            on_watchlist = True
        else:
            on_watchlist = False
    else:
        on_watchlist = False

    return render(request, "auctions/listing.html", {
        "listing" : util.find_listing(title),
        "on_watchlist": on_watchlist
    })

def get_watchlist(request):
    pass

def add_watchlist(request):
    pass

def remove_watchlist(request):
    pass

def categories(request):
    return render(request, "auctions/categories.html", {
        "cat": util.get_categories()
    })

def category(request, cat):
    listings = util.listings_by_category(cat)
    return render(request, "auctions/category.html", {
        "listings": listings,
        "cat": cat
    })
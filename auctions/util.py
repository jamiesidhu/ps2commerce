from .models import Listing

def get_listings():
    """
    Returns a list of active listings
    """
    listings = Listing.objects.all()
    return listings

def find_listing(title):
    listing = Listing.objects.filter(title=title)
    return listing.first()

def get_categories():
    listings = Listing.objects.all()
    categories = []
    for listing in listings:
        categories.append(listing.category)
    return categories

def listings_by_category(category):
    listings = Listing.objects.filter(category=category)
    return listings
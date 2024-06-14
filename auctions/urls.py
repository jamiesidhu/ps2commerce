from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("list", views.listitem, name="list"),
    path("listing/<str:title>", views.listing, name="listing"),
    path("watchlist", views.get_watchlist, name="watchlist"),
    path("add_watchlist", views.add_watchlist, name="add_watchlist"),
    path("remove_watchlist", views.remove_watchlist, name="remove_watchlist"),
    path("categories", views.categories, name="categories"),
    path("category/<str:cat>", views.category, name="category")
]

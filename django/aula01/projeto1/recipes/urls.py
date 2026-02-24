from recipes.views import home, contato, sobre
from django.urls import path

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]
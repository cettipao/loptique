from django.urls import path
from .views import *

urlpatterns = [
    #path('', home_view),
    path('genpdf/<int:id>', pdf_view),
]
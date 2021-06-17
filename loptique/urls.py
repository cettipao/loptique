from django.urls import path
from .views import *

urlpatterns = [
    #path('', home_view),
    path('genpdf/<int:id>', pdf_view),
    path('getbalance/<str:tipo>', balance_view),
    path('receta/', receta_view),
    path('varios/', varios_view),
]
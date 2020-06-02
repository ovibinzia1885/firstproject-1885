
from django.urls import path

from . import views

urlpatterns = [
    path('',views.listings_index,name='listings_index'),
    path('<int:listing_id>',views.listing,name='listing'),
    path('search/',views.search,name='search'),
    path('inquiry', views.listing_inquiry, name='listing_inquiry')

]

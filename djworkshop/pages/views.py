from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from Listings.models import Listing
from django.shortcuts import render
from Realtors.models import Realtor
from Listings.model_choices import state_choices, bedroom_choices, price_choices


#
def index(request):
    listing_list=Listing.objects.order_by('-list_date')[:3]
    page = request.GET.get('page', 1)
    paginator = Paginator(listing_list, 2)
    try:
        listing_list = paginator.page(page)

    except PageNotAnInteger:
        # fallback to the first page
        listing_list = paginator.page(1)

    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        listing_list = paginator.page(paginator.num_pages)

    context={
        'listing_list':listing_list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }

    return render(request,'pages/index.html',context)




def about(request):
    team = Realtor.objects.order_by('-contact_date')[:3]
    seller_of_month = Realtor.objects.filter(is_mvp=True).first()

    context = {
        'team': team,
        'seller_of_month': seller_of_month
    }
    return render(request,'pages/about.html',context)


def listview(request):
    listview=Listing.objects.filter(is_published=True)
    context={
        'listview':listview
    }
    return render(request,'pages/listview.html',context)
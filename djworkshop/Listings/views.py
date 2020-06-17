from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from . models import Listing,Inquiry
from .model_choices import price_choices, state_choices, bedroom_choices
# from .models import * # Bad Practise
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
# listings app view



def listings_index(request):
    listing_list=Listing.objects.all()
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
        'listing_list':listing_list
    }
    return render(request,'Listings/listings.html',context)

def listing(request,listing_id):

    listing_ = Listing.objects.get(id=listing_id)
    return render(request, 'Listings/listing.html', {'listing': listing_})

def search(request):

    get_method = request.GET.copy()
    keywords = get_method.get('keywords') or None
    city = get_method.get('city') or None
    print(keywords, city)

    listing_list=Listing.objects.all()

    if 'keywords' is not None:
        keyword = get_method['keywords']

        listing_list = listing_list.filter(des2__icontains=keyword)

        # city
    if 'city' is not None:
        city = get_method['city']
        listing_list = listing_list.filter(city__iexact=city)
                # state
    if 'state' in get_method:
        state = get_method['state']
        listing_list = listing_list.filter(state__iexact=state)

            # bedroom
    if 'bedrooms' in get_method:
        bedrooms = get_method['bedrooms']
        print(bedrooms)
        listing_list = listing_list.filter(bedroom__lte=int(bedrooms))  # 5 <= 1, 2, 3, 4, 5
        print(listing_list)
                    # price
    if 'price' in get_method:
        price = get_method['price']
        listing_list = listing_list.filter(price__lte=int(price))

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'get_method': get_method,
        'listing_list': listing_list
    }
    return render(request,'Listings/search.html',context)

def listing_inquiry(request):
    if request.method == "POST":
        get_method = request.POST.copy()
        listing = get_method.get('listing')
        phone = get_method.get('phone')
        message = get_method.get('message')


        listing_object = Listing.objects.get(title=listing)

        inquiry_exist = Inquiry.objects.filter(listing=listing_object, user=request.user)

        if not inquiry_exist:
            Inquiry.objects.create(listing=listing_object, user=request.user, phone=phone, message=message)

            messages.success(request, 'Inquiry Message Sent Successfully!. Our Team Will Contact You Through Mail.')
        else:
            messages.error(request, 'You Inquiried Already!')

        send_mail(
            'Inquiry Listing From DJRE',
            'Thank you for contacting us. We Will contact you soon. DJRE Team.',
            settings.EMAIL_HOST_USER,
            [request.user.email, settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

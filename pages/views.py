from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from listings.choices import bedroom_choices, state_choices, price_choices
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listing = Listing.objects.order_by('-id').filter(is_published=True)
    paginator = Paginator(listing, 3)  # Show 3 contacts per page
    page_number = request.GET.get('page')
    page_listing = paginator.get_page(page_number)
    dict = { 'listings': page_listing,
             "bedroom_choices" : bedroom_choices,
             "state_choices": state_choices,
             "price_choices": price_choices,
             }
    return render(request, 'pages/index.html', dict)

def about(request):
    realtor = Realtor.objects.order_by('-hired_date')
    seller = Realtor.objects.all().filter(seller_of_month=True)
    dict = {'realtors': realtor,
            'seller_of_month': seller }
    return render(request, "pages/about.html", dict)

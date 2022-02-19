from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Listing
from  .choices import price_choices, bedroom_choices, state_choices
from realtors.models import Realtor
# Create your views here.
def listings(request):
    listing = Listing.objects.order_by('-id').filter(is_published=True)
    paginator = Paginator(listing, 3)  # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_listing = paginator.get_page(page_number)
    dict = {'listings': page_listing}
    return render(request, 'listings/listings.html', dict)

def search(request):
    query_set = Listing.objects.all()
    # picks keywords written in url and checks in description
    if 'keywords' in request.GET:
        keywords= request.GET['keywords']
        if keywords:
            query_set = Listing.objects.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set = query_set.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_set = query_set.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms= request.GET['bedrooms']
        if bedrooms:
            query_set=query_set.filter(bedrooms__gte = bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_set = query_set.filter(price__lte = price)


    dict = {
        "listings" : query_set,
        "price_choices" : price_choices,
        "bedroom_choices": bedroom_choices,
        "state_choices" : state_choices,
        "values_stay": request.GET,
    }
    return render(request, 'listings/search.html', dict)

def listing(request,pk):
    listing = get_object_or_404(Listing, pk=pk)
    realtor = Realtor.objects.all()
    dict =  {'realtors': realtor,
             'listings': listing
             }
    return render(request, 'listings/listing.html', dict)
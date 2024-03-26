from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm
from django.db.models import Q



def sell(request):
    form = PropertyForm(request.POST, request.FILES)
    if request.method == "POST":

        print('inside post')
        if form.is_valid():
            form.save()
            return render(request, 'properties/success.html')
    # else:
    #     form = UserRegForm()
    return render(request, 'properties/sell.html', {'form': form})



def luxury_estate(request):
    properties = Property.objects.filter(property_category='luxury')
    return render(request, 'properties/property_list.html', {'properties': properties})



def oceanfront_retreats(request):
    properties = Property.objects.filter(property_category='oceanfront')
    return render(request, 'properties/property_list.html', {'properties': properties})


def urban_living(request):
    properties = Property.objects.filter(property_category='urban')
    return render(request, 'properties/property_list.html', {'properties': properties})


def countryside_escapes(request):
    properties = Property.objects.filter(property_category='countryside')
    return render(request, 'properties/property_list.html', {'properties': properties})


def property_search(request):
    search_query = request.GET.get('search_query', '')
    location_filter = request.GET.get('location', '')
    category_filter = request.GET.get('category', '')
    features_filter = request.GET.get('features', '')

    # Use Q objects to perform an OR search across multiple fields
    properties = Property.objects.filter(
        Q(property_title__icontains=search_query) |
        Q(property_location__icontains=search_query) |
        Q(property_category__icontains=search_query) |
        Q(property_features__icontains=search_query)
    )

    return render(request, 'properties/search_results.html', {'properties': properties, 'search_query': search_query})

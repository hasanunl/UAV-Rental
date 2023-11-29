from django.shortcuts import render

from .models import Uav, Brand, UavInstance, Category

def index(request):

    num_uav_models = Uav.objects.all().count()
    num_instances = UavInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = UavInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_brands = Brand.objects.count()

    context = {
        'num_uav_models': num_uav_models,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_brands': num_brands,
    }

    return render(request, 'index.html', context=context)
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

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

class UavListView(generic.ListView):
    model = Uav
    
class UavDetailView(generic.DetailView):
    model = Uav

class RentedUavsByUserListView(LoginRequiredMixin,generic.ListView):
    model = UavInstance
    template_name = 'rental/uavinstance_list_rented_user.html'

    def get_queryset(self):
        return (
            UavInstance.objects.filter(renter=self.request.user)
            .filter(status__exact='r')
            .order_by('return_date')
        )

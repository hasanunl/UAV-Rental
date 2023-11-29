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

import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from rental.forms import RenewUavForm

@login_required
@permission_required('rental.can_mark_returned', raise_exception=True)
def renew_uav_member(request, pk):
    uav_instance = get_object_or_404(UavInstance, pk=pk)

    if request.method == 'POST':

        form = RenewUavForm(request.POST)

        if form.is_valid():
            uav_instance.return_Date = form.cleaned_data['renewal_date']
            uav_instance.save()

            return HttpResponseRedirect(reverse('all-rented'))

    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=4)
        form = RenewUavForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'uav_instance': uav_instance,
    }

    return render(request, 'rental/uav_renew_member.html', context)

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import UavInstance

class UavInstanceCreate(CreateView):
    model = UavInstance
    fields = ['Uav', 'return_date', 'renter', 'status']
    success_url = reverse_lazy('uavs')
    permission_required = 'rental.add_uavinstance'


class UavInstanceUpdate(UpdateView):
    model = UavInstance
    fields = ['Uav', 'return_date', 'renter', 'status']
    success_url = reverse_lazy('uavs')
    permission_required = 'rental.change_uavinstance'


class UavInstanceDelete(DeleteView):
    model = UavInstance
    success_url = reverse_lazy('uavs')
    permission_required = 'rental.delete_uavinstance'
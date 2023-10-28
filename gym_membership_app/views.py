from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Membership
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from datetime import date

# Create your views here.


def membership_list(request):
    members = Membership.objects.all()
    today = date.today()
    for member in members:
        membership_date = member.membership_date
        sessions_remain = (today-membership_date).days
        sessions_remain = 30-sessions_remain
        member.membership_remain = sessions_remain
        member.save()

    return render(request, 'membership_list.html', {
        'members': members,
    })


class MembershipCreate(CreateView):
    model = Membership
    fields = '__all__'
    template_name = 'membership_create.html'
    success_url = reverse_lazy('membership_list')


class MembershipDelete(DeleteView):
    model = Membership
    context_object_name = 'member'
    template_name = 'membership_delete.html'
    success_url = reverse_lazy('membership_list')


class MembershipView(DetailView):
    model = Membership
    context_object_name = 'member'
    template_name = 'membership_view.html'


class MembershipRenewal(UpdateView):
    model = Membership
    fields = '__all__'
    template_name = 'membership_renewal.html'
    success_url = reverse_lazy('membership_list')

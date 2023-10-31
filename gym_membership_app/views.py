from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Membership
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.detail import DetailView
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('membership_list')


class Register(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        if user is None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('membership_list')
        return super(Register, self).get(*args, **kwargs)


def membership_list(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('login')


class MembershipCreate(CreateView, LoginRequiredMixin):
    model = Membership
    fields = '__all__'
    template_name = 'membership_create.html'
    success_url = reverse_lazy('membership_list')


class MembershipDelete(DeleteView, LoginRequiredMixin):
    model = Membership
    context_object_name = 'member'
    template_name = 'membership_delete.html'
    success_url = reverse_lazy('membership_list')


class MembershipView(DetailView, LoginRequiredMixin):
    model = Membership
    context_object_name = 'member'
    template_name = 'membership_view.html'


class MembershipRenewal(UpdateView, LoginRequiredMixin):
    model = Membership
    fields = '__all__'
    template_name = 'membership_renewal.html'
    success_url = reverse_lazy('membership_list')

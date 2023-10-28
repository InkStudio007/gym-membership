from django.urls import path
from .views import MembershipCreate, MembershipDelete, MembershipView, MembershipRenewal
from . import views

urlpatterns = [
    path('', views.membership_list, name='membership_list'),
    path('add-member', MembershipCreate.as_view(), name='membership_create'),
    path('delete-member/<int:pk>/', MembershipDelete.as_view(), name='membership_delete'),
    path('view-member/<int:pk>/', MembershipView.as_view(), name='membership_view'),
    path('renewal-member/<int:pk>/', MembershipRenewal.as_view(), name='membership_renewal'),
]
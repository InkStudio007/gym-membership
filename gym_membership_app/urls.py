from django.urls import path
from .views import MembershipCreate, MembershipDelete, MembershipView, MembershipRenewal, Login, Register
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),

    path('', views.home, name='home'),
    path('members/', views.membership_list, name='membership_list'),
    path('add-member/', MembershipCreate.as_view(), name='membership_create'),
    path('delete-member/<int:pk>/', MembershipDelete.as_view(), name='membership_delete'),
    path('view-member/<int:pk>/', MembershipView.as_view(), name='membership_view'),
    path('renewal-member/<int:pk>/', MembershipRenewal.as_view(), name='membership_renewal'),
]
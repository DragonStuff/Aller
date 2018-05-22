from django.urls import path, include
from rest_framework import routers
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django.db import transaction

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'person', api.PersonViewSet)
router.register(r'car', api.CarViewSet)
router.register(r'location', api.LocationViewSet)


urlpatterns = (
    # URLs for Django Rest Framework API
    path('api/v1/', include(router.urls)),
    # View for dashboard
    path('dashboard/', login_required(views.dashboard), name='dashboard'),
    path('dashboard/update/', login_required(transaction.atomic(views.update_profile)), name='dashboard_update')
)

urlpatterns += (
    # Dashboard URLs
    path('', views.IndexView.as_view(), name="IndexView"),
    path('rating/<str:paymentid>/<int:rating>/', login_required(views.rate), name="RatingView"),
)

urlpatterns += (
    # urls for Person
    path('person/', views.PersonListView.as_view(), name='AllerNow_person_list'),
    path('person/create/', login_required(views.PersonCreateView.as_view()), name='AllerNow_person_create'),
    path('person/detail/<slug:slug>/', views.PersonDetailView.as_view(), name='AllerNow_person_detail'),
    path('person/update/<slug:slug>/', login_required(views.PersonUpdateView.as_view()), name='AllerNow_person_update'),
)

urlpatterns += (
    # urls for Car
    path('car/', views.CarListView.as_view(), name='AllerNow_car_list'),
    path('car/<int:page>', views.CarListView.as_view(), name='AllerNow_car_list'),
    path('car/<slug:slug>', RedirectView.as_view(pattern_name='AllerNow_car_detail'), name='AllerNow_car_detail'),
    path('car/create/', login_required(views.CarCreateView.as_view()), name='AllerNow_car_create'),
    path('car/detail/<slug:slug>/', views.CarDetailView.as_view(), name='AllerNow_car_detail'),
    path('car/update/<slug:slug>/', login_required(views.CarUpdateView.as_view()), name='AllerNow_car_update'),
    path('car/search/', views.CarSearchListView.as_view(), name='car_search_list_view'),
)

urlpatterns += (
    # urls for Location
    path('location/', views.LocationListView.as_view(), name='AllerNow_location_list'),
    path('location/create/', login_required(views.LocationCreateView.as_view()), name='AllerNow_location_create'),
    path('location/detail/<slug:slug>/', views.LocationDetailView.as_view(), name='AllerNow_location_detail'),
    path('location/update/<slug:slug>/', login_required(views.LocationUpdateView.as_view()), name='AllerNow_location_update'),
)

urlpatterns += (
    # urls for Payment
    path('payment/', login_required(views.PaymentListView.as_view()), name='AllerNow_payment_list'),
    path('payment/create/', login_required(views.PaymentCreateView.as_view()), name='AllerNow_payment_create'),
    path('payment/detail/<slug:slug>/', login_required(views.PaymentDetailView.as_view()), name='AllerNow_payment_detail'),
    path('payment/update/<slug:slug>/', login_required(views.PaymentUpdateView.as_view()), name='AllerNow_payment_update'),
    path('payment/choice/<int:carChoice>/<int:days>/', login_required(views.create_payment), name='AllerNow_pay_car'),
)
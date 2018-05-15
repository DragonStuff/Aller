from django.urls import path, include
from rest_framework import routers
from django.views.generic.base import RedirectView

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'person', api.PersonViewSet)
router.register(r'car', api.CarViewSet)
router.register(r'location', api.LocationViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Person
    path('person/', views.PersonListView.as_view(), name='AllerNow_person_list'),
    path('person/create/', views.PersonCreateView.as_view(), name='AllerNow_person_create'),
    path('person/detail/<slug:slug>/', views.PersonDetailView.as_view(), name='AllerNow_person_detail'),
    path('person/update/<slug:slug>/', views.PersonUpdateView.as_view(), name='AllerNow_person_update'),
)

urlpatterns += (
    # urls for Car
    path('car/', views.CarListView.as_view(), name='AllerNow_car_list'),
    path('car/create/', views.CarCreateView.as_view(), name='AllerNow_car_create'),
    path('car/detail/<slug:slug>/', views.CarDetailView.as_view(), name='AllerNow_car_detail'),
    path('car/<slug:slug>/', RedirectView.as_view(pattern_name='AllerNow_car_detail'), name='redirectCar'),
    path('car/update/<slug:slug>/', views.CarUpdateView.as_view(), name='AllerNow_car_update'),
)

urlpatterns += (
    # urls for Location
    path('location/', views.LocationListView.as_view(), name='AllerNow_location_list'),
    path('location/create/', views.LocationCreateView.as_view(), name='AllerNow_location_create'),
    path('location/detail/<slug:slug>/', views.LocationDetailView.as_view(), name='AllerNow_location_detail'),
    path('location/update/<slug:slug>/', views.LocationUpdateView.as_view(), name='AllerNow_location_update'),
)

urlpatterns += (
    # urls for Payment
    path('payment/', views.PaymentListView.as_view(), name='app_name_payment_list'),
    path('payment/create/', views.PaymentCreateView.as_view(), name='app_name_payment_create'),
    path('payment/detail/<slug:slug>/', views.PaymentDetailView.as_view(), name='app_name_payment_detail'),
    path('payment/update/<slug:slug>/', views.PaymentUpdateView.as_view(), name='app_name_payment_update'),
)
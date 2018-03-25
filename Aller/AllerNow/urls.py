from django.urls import path, include
from rest_framework import routers

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
    path('AllerNow/person/', views.PersonListView.as_view(), name='AllerNow_person_list'),
    path('AllerNow/person/create/', views.PersonCreateView.as_view(), name='AllerNow_person_create'),
    path('AllerNow/person/detail/<slug:slug>/', views.PersonDetailView.as_view(), name='AllerNow_person_detail'),
    path('AllerNow/person/update/<slug:slug>/', views.PersonUpdateView.as_view(), name='AllerNow_person_update'),
)

urlpatterns += (
    # urls for Car
    path('AllerNow/car/', views.CarListView.as_view(), name='AllerNow_car_list'),
    path('AllerNow/car/create/', views.CarCreateView.as_view(), name='AllerNow_car_create'),
    path('AllerNow/car/detail/<slug:slug>/', views.CarDetailView.as_view(), name='AllerNow_car_detail'),
    path('AllerNow/car/update/<slug:slug>/', views.CarUpdateView.as_view(), name='AllerNow_car_update'),
)

urlpatterns += (
    # urls for Location
    path('AllerNow/location/', views.LocationListView.as_view(), name='AllerNow_location_list'),
    path('AllerNow/location/create/', views.LocationCreateView.as_view(), name='AllerNow_location_create'),
    path('AllerNow/location/detail/<slug:slug>/', views.LocationDetailView.as_view(), name='AllerNow_location_detail'),
    path('AllerNow/location/update/<slug:slug>/', views.LocationUpdateView.as_view(), name='AllerNow_location_update'),
)


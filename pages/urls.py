from django.urls import path
from django.views.generic.base import View
from pages.views import AboutPageView, HomePageView

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about')
]
from django.urls import path
from .views import CompareView

urlpatterns = [ (
    path('compare-addresses/', CompareView.as_view(), name ='compare-addresses')
)]
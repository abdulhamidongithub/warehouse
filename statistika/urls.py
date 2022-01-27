from django.urls import path
from .views import StatsView, StatsUpdate

urlpatterns = [
    path('', StatsView.as_view(), name='stats'),
    path('update/<int:pk>', StatsUpdate.as_view(), name='stats-update'),
]
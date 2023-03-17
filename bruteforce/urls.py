from django.urls import path
from .views import BruteForceLoginView, DashboardView

urlpatterns = [
    path('admin/login/', BruteForceLoginView.as_view(), name='login'),
    path('', DashboardView.as_view(), name='index'),
]
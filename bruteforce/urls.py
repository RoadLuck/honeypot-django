from django.urls import path
from .views import BruteForceLoginView, DashboardView, attack_stats

urlpatterns = [
    path('wp-login.php', BruteForceLoginView.as_view(), name='login'),
     path('admin/attack_stats/', attack_stats, name='attack_stats'),
    path('', DashboardView.as_view(), name='index'),
]
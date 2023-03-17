from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .models import BruteForceAttack

class BruteForceLoginView(LoginView):
    template_name = 'admin/login.html'
    success_url = reverse_lazy('admin:index')

    def form_invalid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        ip_address = self.request.META.get('REMOTE_ADDR')
        
        BruteForceAttack.objects.create(
            username=username,
            password=password,
            ip_address=ip_address,
        )
        
        return super().form_invalid(form)


class DashboardView(TemplateView):
    template_name = 'index.html'
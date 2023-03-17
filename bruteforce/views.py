from django.contrib.auth.views import LoginView
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render

from .models import BruteForceAttack
from .utils import get_location


class BruteForceLoginView(LoginView):
    template_name = 'admin/login.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        ip_address = self.request.META.get('REMOTE_ADDR')
        try:
            location = get_location(ip_address)
            if location['country'] == None:
                location = {'country': 'N-N'}

        except:
            location = {
                'country': 'N-N'
            }
        BruteForceAttack.objects.create(
            username=username,
            password=password,
            ip_address=ip_address,
            country=location['country'],
            is_success=False
        )
        
        return super().form_invalid(form)


class DashboardView(TemplateView):
    template_name = 'index.html'


@staff_member_required
def attack_stats(request):
    total_attacks = BruteForceAttack.objects.count()
    attacks = BruteForceAttack.objects.all()
    attack_countries = {}

    for attack in attacks:
         
        if attack.country:
            country_name = attack.country
        else:
            country_name = "N-N"
        if country_name not in attack_countries:
            attack_countries[country_name] = 0
        attack_countries[country_name] += 1
        
    context = {
        'total_attacks': total_attacks,
        'attack_countries': attack_countries,
    }
    return render(request, 'attack_stats.html', context)
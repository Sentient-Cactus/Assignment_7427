from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address


class AddressView(CreateView):
    model = Address
    fields = ['address']
    template_name = 'activity/create_activity.html'
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['access_token'] = 'pk.eyJ1Ijoia21raW0wMSIsImEiOiJja3YyNHZ6aDQzODE4MnJueW8xb2dreHN6In0.E4vmyvWw7zt-OKTZL-9gTw'
        context['addresses'] = Address.objects.all()
        return context

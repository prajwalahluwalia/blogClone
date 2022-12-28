from django.urls import reverse
from django.views.generic import TemplateView

class Homepage(TemplateView):
    template_name = 'index.html'
    
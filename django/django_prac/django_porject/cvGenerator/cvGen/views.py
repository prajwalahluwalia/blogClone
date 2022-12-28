from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from . import models, forms
from django.views.generic import ListView, CreateView
from django.http import HttpResponse
from django.template import loader
import io
import pdfkit

# Create your views here.

def resume(request, pk):
    user_profile = models.UserProfile.objects.get(pk=pk)
    template = loader.get_template('cvGen/resume.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size':'Letter',
        'encoding': 'utf-8'
    }
    pdf = pdfkit.from_string(html, False, options)
    
    response = HttpResponse(pdf, content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'
    return response

def cvList(request):
    profiles = models.UserProfile.objects.all()
    return render(request,'cvGen/profile_list.html', {'profiles':profiles})
    
class CreateCv(CreateView):
    fields = ('name', 'email', 'phone', 'summary', 'degree', 'school', 'university', 'previous_work', 'skills')
    model = models.UserProfile

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)
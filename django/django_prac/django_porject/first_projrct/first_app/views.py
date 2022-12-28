from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, WebPage
from first_app.forms import FormName

# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}

    return render(request, 'first_app/index.html', context=date_dict)

def form_view(request):
    form = FormName()

    if request.method == "POST":
        form = FormName(request.POST)

        if form.is_valid():
            print("Validation Success!!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+ form.cleaned_data['text'])


    return render(request, 'first_app/form.html', {'form':form})
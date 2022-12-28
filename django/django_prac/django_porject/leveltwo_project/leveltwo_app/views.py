from django.shortcuts import render
from leveltwo_app.models import User
from leveltwo_app.forms import NewUserForm
# Create your views here.


def index(request):
    return render(request, 'leveltwo_app/index.html')

def user(request):
    user_data = User.objects.order_by('first_name')
    users = {'user_record': user_data}

    return render(request, 'leveltwo_app/users.html', context=users)

def form_view(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            return render(request, 'level_two_app/error.html')
    return render(request, 'leveltwo_app/user.html', {'form' : form})
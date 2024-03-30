from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.http import HttpResponse
from django.template import loader
from .models import Member

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'registrationform.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

# Create your views here.

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
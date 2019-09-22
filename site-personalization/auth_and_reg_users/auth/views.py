from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(
        request,
        'home.html'
    )

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'],
                None,
                form.cleaned_data['password1']
            )
            user.save()
            login(request, user)
            return redirect('home')
    return render(
        request,
        'signup.html',
        {'form': form},
    )

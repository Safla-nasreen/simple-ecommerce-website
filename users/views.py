
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm
from .models import UserProfile, Company
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            user_type = form.cleaned_data['user_type']
            user_profile = UserProfile.objects.create(user=user, user_type=user_type)

            # If the user type is 'company', create a Company instance
            if user_type == 'company':
                Company.objects.create(
                    user_profile=user_profile,
                    name=form.cleaned_data['company_name'],
                    address=form.cleaned_data['address'],
                    phone_number=form.cleaned_data['phone_number'],
                    email=user.email
                )

            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register_user.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserProfileInfoForm


def base(request):
    return render(request, 'base.html')


def cs_signup(request):
    already_registered = cs_profile
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('Encontrado!')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            api_signin(request, user, user.password)
            return HttpResponseRedirect(reverse('csapp:profile'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'registration/signup.html', {'user_form': user_form,
                                                        'profile_form': profile_form,
                                                        'registered': registered,
                                                        'already_registered': already_registered, })


def api_signin(request, username=None, password=None):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
        return HttpResponseRedirect(reverse('csapp:profile'))


def cs_signin(request):
    _errors = ''
    user = None
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('csapp:profile'))
            else:
                _errors = 'Inactive account'
        else:
            _errors = '* Informações de login incorretas!'

    return render(request, 'registration/signin.html', {'errors': _errors, 'user': user})


@login_required
def cs_password_change(request):
    _errors = None
    form = None
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse('csapp:profile'))
        else:
            _errors = form.errors
    return render(request, 'registration/change_password.html', {'form': form, 'errors': _errors})


@login_required
def cs_profile(request):
    circle_rate = None
    return render(request, 'profile.html', {'circle': circle_rate})


@login_required
def cs_exit(request):
    logout(request)
    return HttpResponseRedirect(reverse('csapp:signin'))


def cs_search(request):
    return render(request, "search.html")



"""

        profile_form = UserProfileInfoForm(data=request.POST)
        
        and profile_form.is_valid()
        
        , profile_form.errors
        
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('Encontrado!')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            
                    profile_form = UserProfileInfoForm()
                                                                  'profile_form': profile_form,
"""
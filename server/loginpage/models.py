from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from userprofile.models import user_profile


# Create your models here.
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail ID already exists!')
                return redirect('signup/')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken!')
                return redirect('signup/')
            else:
                user = User.objects.create_user(name=name,username=username,email=email,password=password)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = user_profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('login/')
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('signup/')
    else:
        return redirect('registration.html')

            

  
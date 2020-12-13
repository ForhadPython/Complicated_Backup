from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from product.models import Category
from user.models import UserProfile


def index(request):
    return HttpResponse("Hello This Is a User page")


def login_form(request):
    if request.method == 'POST':  # check post
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            return HttpResponseRedirect('/')
        else:
            messages.success(request, " Username And Password is Incorrect !! ")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'login_form.html',context)


def signup_form(request):
    category = Category.objects.all()
    context = {'category': category}
    return HttpResponse("Hello This Is a User Signup")


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')
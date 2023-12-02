from django.shortcuts import render, redirect
from shared.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm
# Import Pagination Stuff
from django.core.paginator import Paginator
def loginPage(request):
    page = 'login'
    context = {'page': page}

    if request.user.is_authenticated:
        return redirect('test')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=email)
        except:
            messages.error(request, 'User does not exist')
            return render(request, 'candidat/login.html', context)

                 # Check if the user's role is not equal to 1
        if user.role != 1:
            messages.error(request, 'You do not have permission to login')
            return render(request, 'candidat/login.html', context)
        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('test')
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'candidat/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginc')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.role=0
            user.save()
            login(request, user)
            return redirect('test')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'candidat/login.html', {'form': form})

def test(request):
 return render(request, 'recruter/test.html')
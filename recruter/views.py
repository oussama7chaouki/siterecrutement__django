from django.shortcuts import render, redirect
from shared.models import User
from .models import Job,Candidature
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm
# Import Pagination Stuff
from django.core.paginator import Paginator


def test(request):
 return render(request, 'recruter/test.html')

def offer(request):
 job_list = Job.objects.all().order_by('-id_job')
 p = Paginator(Job.objects.all().order_by('-id_job'), 5)
 page = request.GET.get('page')
 jobs = p.get_page(page)
 nums = "a" * jobs.paginator.num_pages
 user_id = request.user.id
 return render(request, 'recruter/jobs.html', 
		{'job_list': job_list,
		'offers': jobs,
		'nums':nums
        ,'recruter': user_id}
		)
#  offers = [
#     {"id": 1, "title": "Software Engineer", "domain": "Information Technology", "date": "2023-11-28"},
#     {"id": 2, "title": "Financial Analyst", "domain": "Finance", "date": "2023-11-25"},
#     {"id": 3, "title": "Marketing Manscorer", "domain": "Marketing", "date": "2023-11-20"},
#     ]
 

def jobcans(request):
 job_list = Job.objects.all().order_by('-id_job')
 p = Paginator(Job.objects.all().order_by('-id_job'), 4)
 page = request.GET.get('page')
 jobs = p.get_page(page)
 nums = "a" * jobs.paginator.num_pages
 return render(request, 'recruter/jobcans.html', 
		{'job_list': job_list,
		'jobcans': jobs,
		'nums':nums
        }
		)

def jobcan(request,pk):
   datas = [
      {'name': 'Alice', 'score': 25, 'email': 'alice@example.com'},
      {'name': 'Bob', 'score': 30, 'email': 'bob@example.com'},
      {'name': 'Charlie', 'score': 22, 'email': 'charlie@example.com'},
   ]
   context = {'datas': datas}
   return render(request, 'recruter/jobcan.html',context)

def loginPage(request):
    page = 'login'
    context = {'page': page}

    if request.user.is_authenticated:
        return redirect('offer')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=email)
        except:
            messages.error(request, 'User does not exist')
            return render(request, 'recruter/login.html', context)

                 # Check if the user's role is not equal to 1
        if user.role != 1:
            messages.error(request, 'You do not have permission to login')
            return render(request, 'recruter/login.html', context)
        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('offer')
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'recruter/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('offer')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'recruter/login.html', {'form': form})

       

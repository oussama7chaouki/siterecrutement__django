from django.shortcuts import render, redirect
from shared.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm
from .models import Skill,Language,Formation,Experience,Information,Profile
from recruter.models import Candidature


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
        if user.role != 0:
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
 return render(request, 'candidat/test.html')

def compte(request):
 user_id = request.user
 experience=Experience.objects.filter(user_id=user_id)
 formation=Formation.objects.filter(user_id=user_id)
#  print(formation)
 print(experience)
 skill=Skill.objects.filter(user_id=user_id)
 language=Language.objects.filter(user_id=user_id)
 context = {
        'experience': experience,
        'formation':formation,
        'skill':skill,
        'language':language,
    }
 return render(request, 'candidat/compte.html',context)

def candidature(request):
    
    candidatures = Candidature.objects.filter(candidat=request.user).values('id_candidature','date','job__job_title','job__recruter__name','status')
    
    context = {
        'candidatures': candidatures,
    }
    return render(request, 'candidat/candida.html', context)
from django.http import JsonResponse

def delete_candidature(request):
    if request.method == 'POST':
        candidature_id = request.POST.get('id_candidature')
        try:
            candidature = Candidature.objects.get(id_candidature=candidature_id)
            candidature.delete()
            return JsonResponse({'status': 'success'})
        except Candidature.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Candidature not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
def view_score(request, candidature_id):
    candidature = Candidature.objects.filter(id_candidature=candidature_id).first()
    
    if candidature is not None:
        # Extract relevant data from the candidature
        score_data = {
            'score': candidature.score,
            'reqfor': candidature.reqfor,
            'reqexp': candidature.reqexp,
            'reqskill': candidature.reqskill,
        }

        return JsonResponse(score_data)
    else:
        return JsonResponse({'error': 'Candidature not found'}, status=404)

       

def profile_details(request):
    user_id = request.user # Assuming you have the user ID in the session

    try:
        profile = Profile.objects.get(candidat_id=user_id)
    except Profile.DoesNotExist:
        return redirect('profile_form')
    
    context = {
        'profile': profile,
    }

    return render(request, 'candidat/settings.html', context)
def profile_form(request):
    user_id = request.user

    if request.method == 'POST':
        # Récupérez les données du formulaire
        last_name = request.POST.get('nom')
        name = request.POST.get('prenom')
        email=request.POST.get('email')
        date_naissance = request.POST.get('date')
        genre = request.POST.get('genre')
        ville = request.POST.get('ville')
        pays=request.POST.get('pays')
        tel = request.POST.get('tel')
        domaine = request.POST.get('select')

        # Récupérez l'utilisateur actuel
        # Ajout de '.id' pour obtenir l'ID de l'utilisateur

        try:
            profile = Profile.objects.get(candidat_id=user_id)
            # Modifier le profil existant
            profile.last_name = last_name
            profile.name = name
            profile.email =email
            profile.date_naissance = date_naissance
            profile.genre = genre
            profile.ville = ville
            profile.pays=pays
            profile.tel = tel
            profile.domaine = domaine

            profile.save()
        except Profile.DoesNotExist:
            # Créer un nouveau profil
            profile = Profile.objects.create(
                last_name=last_name,
                name=name,
                email=email,
                date_naissance=date_naissance,
                genre=genre,
                ville=ville,
                pays=pays,
                tel=tel,
                domaine=domaine,
                candidat_id=user_id
            )

            
            
        return JsonResponse({'status': 'success'})

    else:
        # Si la méthode n'est pas POST, récupérez le profil existant ou créez un nouveau
        try:
            profile = Profile.objects.get(candidat_id=user_id)
        except Profile.DoesNotExist:
            profile = {
                "last_name": " ",
                "name": " ",
                "email":" ",
                "date_naissance": " ",
                "genre": " ",
                "ville": " ",
                "pays":"pays",
                "tel": " ",
                "domaine": " ",
            }

    context = {
        'profile': profile,
    }

   
        # If it's a regular form submission, render the HTML template
    return render(request, 'candidat/profilcandidat.html', context)
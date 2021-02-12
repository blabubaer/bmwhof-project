from bmwhof.settings import AUTH_PASSWORD_VALIDATORS
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import PartForm
from .models import Part
#from .forms import TodoForm
#from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

###################### Authetication Process##########################
def signinuser(request):
    if request.method == 'GET':
        return render(request, 'parts/signinuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
#needs to be created
                return redirect('overview')
            except IntegrityError:
                username_error = _("Benutzername wird bereits benutzt. Bitte wählen Sie einen anderen Benutzernamen.")
                return render(request, 'parts/signinuser.html', {'form': UserCreationForm(), 'error':username_error})
        else:
            password_error=_('Die Passwörter stimmen nicht überein.')
            return render(request, 'parts/signinuser.html', {'form': UserCreationForm(), 'error':password_error})


def loginuser(request):
    if request.method=='GET':
        return render(request, 'parts/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            unknownuser_error= _('Der eingegebene Benutzername oder Password sind falsch oder unbekannt. Bitte versuchen Sie es nochmal')
            return render(request, 'parts/loginuser.html',{'form':AuthenticationForm(), 'error':unknownuser_error})
        else:
            login(request, user)
#needs to be created
            return redirect('overview')

@login_required
def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')

############################# App ####################
def home(request):
    return render(request, 'parts/home.html')

@login_required
def addpart(request):
    if request.method == 'GET':
        return render(request, 'parts/addpart.html', {'form':PartForm()})
    else:
        try:
            form = PartForm(request.POST)
            newpart = form.save(commit=False)
            newpart.save()
#needs to be created
            return redirect('overview')
        except:
            data_error = _('Ungültige Daten eingegeben. Bitte nochmal probieren.')
            return render(request, 'parts/addpart.html', {'form':PartForm(),'error':data_error})

def overview(request):
    parts = Part.objects.all()
    return render(request, 'parts/overview.html', {'parts':parts})

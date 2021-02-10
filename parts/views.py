from bmwhof.settings import AUTH_PASSWORD_VALIDATORS
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
#from .forms import TodoForm
#from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _


def signinuser(request):
    if request.method == 'GET':
        return render(request, 'parts/signinuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('overview')
            except IntegrityError:
                username_error = _("Benutzername wird bereits benutzt. Bitte wählen Sie einen anderen Benutzernamen.")
                return render(request, 'parts/signinuser.html', {'form': UserCreationForm(), 'error':username_error})



from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'home/welcome.html', {'today': datetime.today()})

# Block access to webpage if a user isn't logged in
@login_required
def authorized(request):
	return render(request, 'home/authorized.html', {})

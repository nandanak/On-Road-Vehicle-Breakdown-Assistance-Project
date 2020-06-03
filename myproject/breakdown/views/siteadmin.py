from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from breakdown.forms import CustSignupForm, MechSignupForm, ProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from ..decorators import mechanic_required
from ..models import User
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
# Create your views here.

def approveget(request):
	getmechs = User.objects.filter(is_mechanic=1)
	return render(request, 'homepage/siteadmin/adapprove.html',{'getmechs': getmechs})

def approve(request):
	getmechs_item = get_object_or_404(User, pk=pk)
	getmechs_item.is_approved = True if getmechs_item.is_approved == False else false
	getmechs_item.save(update_fields=['is_approved'])
	messages.success(request, 'Mechanic Approved')
	return redirect('approveget')

def adapprove(request):
	return render(request, 'homepage/siteadmin/adapprove.html', {})

def adafterlogin(request):
	return render(request, 'homepage/siteadmin/adafterlogin.html', {})

def admessage(request):
	return render(request, 'homepage/siteadmin/admessage.html', {})

def adprofile(request):
	return render(request, 'homepage/siteadmin/adprofile.html', {})

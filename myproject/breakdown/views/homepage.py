from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from breakdown.forms import CustSignupForm, MechSignupForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from ..decorators import customer_required
from ..models import User
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.

class HomeView(TemplateView):
	template_name = 'homepage/index.html'

def index(request):
	if request.user.is_authenticated:
		if request.user.is_customer:
			return redirect('custafterlogin')
		else:
			return redirect('mechafterlogin')
	return render(request, 'homepage/index.html')

def about(request):
	if request.user.is_authenticated:
		if request.user.is_customer:
			return redirect('custabout')
		else:
			return redirect('custcontact')
	return render(request, 'homepage/about.html')

def services(request):
	if request.user.is_authenticated:
		return redirect('custservices')
	return render(request, 'homepage/services.html')

def signupcust(request):
		return render(request,'homepage/signupcust.html', {})

def signupmech(request):
					return render(request,'homepage/signupmech.html', {})

#def user_login(request):
				#	return render(request, 'homepage/login.html', {})

@login_required
def special(request):
												return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
													logout(request)
													return HttpResponseRedirect(reverse('index'))
def contact(request):
																return render(request, 'contact.html', {})
def aftersignup(request):
	return render(request, 'aftersignup.html', {})
def profile(request):
	return render(request, 'profile.html', {})
def search(request):
	return render(request, 'search.html', {})

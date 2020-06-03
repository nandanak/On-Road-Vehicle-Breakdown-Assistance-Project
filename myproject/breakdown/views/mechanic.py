from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from breakdown.forms import CustSignupForm, MechSignupForm, ProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from ..decorators import mechanic_required
from ..models import User
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
# Create your views here.


class MechanicSignUpView(CreateView):
	model = User
	form_class = MechSignupForm
	template_name = 'homepage/signupmech.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'mechanic'
		return super().get_context_data(**kwargs)


	def form_valid(self, form):
		user = form.save()
		user.refresh_from_db()
		user.profile.fullname = form.cleaned_data.get('fullname')
		user.profile.special = form.cleaned_data.get('special')
		user.profile.email = form.cleaned_data.get('email')
		user.profile.workshop = form.cleaned_data.get('workshop')
		user.profile.location = form.cleaned_data.get('location')
		user.profile.city = form.cleaned_data.get('city')
		user.profile.contact = form.cleaned_data.get('contact')
		user.profile.username = form.cleaned_data.get('username')
		user.profile.password = form.cleaned_data.get('password')
		user.profile.bio = form.cleaned_data.get("bio")
		login(self.request, user)
		return redirect('mechaftersignup')

def mechcontact(request):
	return render(request, 'homepage/mechanic/mechcontact.html', {})

def mechprofile(request):
	return render(request, 'homepage/mechanic/mechprofile.html', {})


def user_login(request):
								if request.method == 'POST':
									email = request.POST.get('email')
									password = request.POST.get('password')
									user = authenticate(email=email, password=password)
									if user:
										if user.is_active:
											login(request,user)
											return HttpResponseRedirect(reverse('index'))
										else:
											return HttpResponse("Your account is inactive.")
									else:
											return HttpResponse("Invalid login details given")
								else:
											return render(request, 'homepage/login.html', {})
@login_required
def special(request):
												return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
													logout(request)
													return HttpResponseRedirect(reverse('index'))
def services(request):
																	return render(request, 'services.html', {})
def mechaftersignup(request):
	return render(request, 'homepage/mechanic/mechaftersignup.html', {})
def mechafterlogin(request):
	return render(request, 'homepage/mechanic/mechafterlogin.html', {})
def search(request):
	return render(request, 'search.html', {})

from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from breakdown.forms import CustSignupForm, MechSignupForm, ProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from ..decorators import customer_required
from ..models import User, Profile
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.


class CustomerSignUpView(CreateView):
		model = User
		form_class = CustSignupForm
		template_name = 'homepage/signupcust.html'

		def get_context_data(self, **kwargs):
			kwargs['user_type'] = 'customer'
			return super().get_context_data(**kwargs)

		def form_valid(self, form):
			user = form.save()
			user.refresh_from_db()
			user.profile.fullname = form.cleaned_data.get('fullname')
			user.profile.email = form.cleaned_data.get('email')
			user.profile.location = form.cleaned_data.get('location')
			user.profile.city = form.cleaned_data.get('city')
			user.profile.contact = form.cleaned_data.get('contact')
			user.profile.username = form.cleaned_data.get('username')
			user.profile.password = form.cleaned_data.get('password')
			login(self.request, user)
			return redirect('custaftersignup')

def custabout(request):
	mechs = User.objects.filter(is_approved=1)
	return render(request, 'homepage/customer/custabout.html', {'mechs': mechs})
def custcontact(request):
	return render(request, 'homepage/customer/custcontact.html', {})
def custservices(request):
	mechs = User.objects.all()
	return render(request, 'homepage/customer/custservices.html', {'mechs': mechs})
def custaftersignup(request):
	return render(request, 'homepage/customer/custaftersignup.html', {})
def custafterlogin(request):
	return render(request, 'homepage/customer/custafterlogin.html', {})

def custprofile(request):
#	if request.method == 'POST':
#		form = ProfileForm(request.POST)
#		if form.is_valid():
#			user = form.save()
#			user.refresh_from_db()
#			user.profile.fullname = user.profile.fullname
#			user.profile.email = user.profile.email
#			user.profile.location = form.cleaned_data.get('location')
#			user.profile.city = form.cleaned_data.get('city')
#			user.profile.contact = form.cleaned_data.get('contact')
#			user.profile.username = user.profile.username
#			user.profile.password = user.profile.password
#			return redirect('custprofile')
#	else:
#		form = ProfileForm()
	return render(request, 'homepage/customer/custprofile.html',{})

class SearchResultsView(ListView):
	model = User
	template_name = 'homepage/customer/searchresults.html'

	def get_queryset(self):
		query = self.request.GET.get('q')
		object_list = User.objects.filter(
			Q(fullname__icontains=query) | Q(special__icontains=query) | Q(workshop__icontains=query) | Q(location__icontains=query) | Q(city__icontains=query)
		)
		return object_list

#class SearchView(ListView):
#	model = User
#	template_name = 'homepage/customer/search.html'


def search(request):
		mechs = User.objects.filter(is_approved=1)
		return render(request, 'homepage/customer/search.html', {'mechs': mechs})


#def mech_list(request):
#	mechs = User.objects.all()
#	print(mechs)
#	return render(request, 'homepage/customer/search.html', {'mechs': mechs})


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

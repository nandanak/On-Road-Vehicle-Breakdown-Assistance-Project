from django.urls import path, include

from .views import homepage, customer, mechanic, siteadmin

urlpatterns = [
    path('', homepage.index, name='index'),
    path('about/', homepage.about, name='about'),
    path('services/', homepage.services, name='services'),
    path('signupcust/', customer.CustomerSignUpView.as_view(), name='signupcust'),
    path('signupmech/', mechanic.MechanicSignUpView.as_view(), name='signupmech'),
    path('approveget/', siteadmin.approveget, name='approveget'),
    path('approve/<int:pk>/', siteadmin.approve, name='approve'),

        path('adafterlogin/', siteadmin.adafterlogin, name='adafterlogin'),
        path('admessage/', siteadmin.admessage, name='admessage'),
        path('adprofile/', siteadmin.adprofile, name='adprofile'),
        path('adapprove/', siteadmin.adapprove, name='adapprove'),
    #path('customer/', include(([
        path('custabout/', customer.custabout, name='custabout'),
        path('custcontact/', customer.custcontact, name='custcontact'),
        path('custservices/', customer.custservices, name='custservices'),
        path('custaftersignup/', customer.custaftersignup, name='custaftersignup'),
        path('custafterlogin/', customer.custafterlogin, name='custafterlogin'),
        path('custprofile/', customer.custprofile, name='custprofile'),
        path('search/', customer.search, name='search'),
#        path('search/', customer.SearchView.as_view(), name='search'),
        path('searchresults/', customer.SearchResultsView.as_view(), name='searchresults'),
    #], 'homepage'), namespace='customer')),

    #path('mechanic/', include(([
        path('mechcontact/', mechanic.mechcontact, name='mechcontact'),
        path('mechaftersignup/', mechanic.mechaftersignup, name='mechaftersignup'),
        path('mechafterlogin/', mechanic.mechafterlogin, name='mechafterlogin'),
        path('mechprofile/', mechanic.mechprofile, name='mechprofile'),
    #], 'homepage'), namespace='mechanic')),
]

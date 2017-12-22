from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^step1/', views.createInvestor, name='createInvestor'),
    url(r'^delete/', views.deleteInvestor, name='deleteInvestor'),
       
    
]
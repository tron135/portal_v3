from django.urls import path
from . import views

urlpatterns = [
    path('<int:candidate_id>',views.candidate, name='candidate'),
    path('',views.candidates,name='candidates'),
    path('addleads',views.addleads,name='teleform'),
    path('enquiry',views.enquiry,name='enquiry'),
    path('admission',views.admission,name='admission')
] 
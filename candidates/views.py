from django.shortcuts import render

# Create your views here.

def candidate(request):
    return render(request, 'candidates/candidate.html')

def candidates(request):
    return render(request, 'candidates/candidates.html')

def addleads(request):
    return render(request, 'candidates/telecallerform.html')

def enquiry(request):
    return render(request, 'candidates/enquiryform.html')

def admission(request):
    return render(request, 'candidates/admission.html')
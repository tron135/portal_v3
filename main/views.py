from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/dashboard.html')

def users(request):
    return render(request, 'main/users.html')
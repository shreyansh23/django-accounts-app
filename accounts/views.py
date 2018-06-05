from django.shortcuts import render, HttpResponse
#from django.http import HttpResponse,
# Create your views here.
def home(request):
    name = "Shreyansh"
    numbers = [1,2,3,4,5]
    args = {'myName':name, 'myNumbers':numbers}

    return render(request, 'accounts/login.html',args)

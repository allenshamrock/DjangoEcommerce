from django.shortcuts import render

# Create your views here.
def user_registration(request):
    return render( request,'account/signup.html')

def user_login(request):
    return render(request,'account/login.html')

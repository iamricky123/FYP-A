from django.shortcuts import render, HttpResponse, redirect
import pyrebase
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_user_model,
    logout
)
from django.contrib.auth.decorators import login_required


config = {
    'apiKey': "AIzaSyD3Q0syggqR2PrD9t2W1znM1EJo5TJk004",
    'authDomain': "my-project-1525487920970.firebaseapp.com",
    'projectId': "my-project-1525487920970",
    'storageBucket': "my-project-1525487920970.appspot.com",
    'messagingSenderId': "270001731276",
    'appId': "1:270001731276:web:7698cc0ffa88af7017f469",
    'measurementId': "G-RDSN74KEYW",
    "databaseURL": "https://my-project-1525487920970-default-rtdb.firebaseio.com/",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()

# Create your views here.
def login_view(request):
    #return HttpResponse("This is my home (/)")
    return render(request, 'login.html')

def postSite (request):
    email = request.POST.get('email')
    passw = request.POST.get('password')
    #data = {"name": "Mortimer 'Morty' Smith"}
    #db.child("users").push(data)
    #user = auth.sign_in_with_email_and_password(email,passw)
    try:
        user=auth.sign_in_with_email_and_password(email, passw)
    except:
        messages="Please check your input. Try again."
        return render(request,"login.html", {"message":messages})

    return render(request, 'main.html')
    
    #message="Invalid credentials. Try again."
    
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

@login_required
def main(request):
    #return HttpResponse("This is my about page (/home)")
    return render(request, 'main.html')

def about(request):
    #return HttpResponse("This is my about page (/about)")
    return render(request, 'about.html')

def contact(request):
    #return HttpResponse("This is my contact (/contact)")
    return render(request, 'contact.html')
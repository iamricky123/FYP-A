# pages/views.py
from django.views.generic import TemplateView
from accounts .models import CustomUser
<<<<<<< HEAD
from accounts.models import UserReport
=======
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import make_password

>>>>>>> 84f261f2eda4a4bf5a3b42e72b6c117076566643

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = CustomUser.objects.all()
        return context


class AboutUsView (TemplateView):
    template_name = 'aboutus.html'

class ContactUsView (TemplateView):
    template_name = 'contactus.html'

class RegisterView (TemplateView):
    template_name = 'registration.html'

class ArachniFormView (TemplateView):
    template_name = 'arachni_form.html'

class ArachniRedirectView (TemplateView):
    template_name = 'arachni_redirect.html'

<<<<<<< HEAD
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history'] = UserReport.objects.all()
        return context
=======
def Userregistration(request):
    if request.method == "POST":
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('password') and request.POST.get('username'):
            saverecord = CustomUser()
            saverecord.first_name = request.POST.get('first_name')
            saverecord.last_name = request.POST.get('last_name')
            saverecord.username = request.POST.get('username')
            saverecord.email = request.POST.get('email')
            saverecord.password = make_password(request.POST.get('password'))
            saverecord.save()
            messages.success(request, "Registered")
            return render (request, 'registration.html')

    else:
        return render(request, 'registration.html')
>>>>>>> 84f261f2eda4a4bf5a3b42e72b6c117076566643

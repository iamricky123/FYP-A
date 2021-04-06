# pages/views.py
from django.views.generic import TemplateView
from accounts .models import CustomUser

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
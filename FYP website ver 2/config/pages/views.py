# pages/views.py
from django.views.generic import TemplateView
from accounts .models import CustomUser
from accounts .models import UserReport, SaveScanID, UserPortReport
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['savescanid'] = SaveScanID.objects.all()
        return context

class ArachniReportView(TemplateView):
    template_name = 'arachni_report.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history'] = UserReport.objects.all()
        return context

class PortScanRedirectView (TemplateView):
    template_name = 'portscan_redirect.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['porthistory'] = UserPortReport.objects.all()
        return context

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

def ShowArachniReport(request):
    if request.method == "POST":
        scan_id = request.POST.get('scan_id')
        
        
        # report = UserReport.objects.raw("SELECT * From accounts_userreport")
        report = UserReport.objects.raw("SELECT * From accounts_userreport Where scan_data=\'"+scan_id+"\'")
        for r in report:
            print(r.scan_data)
        context ={
            'report':report,
            'scan_id':scan_id
        }
        # print (report)

        return render(request, 'arachni_report.html', context)


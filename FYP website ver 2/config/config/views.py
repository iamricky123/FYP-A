from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

# Create your views here.
def external(request):
    uinput = request.POST.get('param')
    out = run([sys.executable,'C:\\Users\\timch_lrogukl\\OneDrive\\Desktop\\FYP-A\\FYP website ver 2\\nmap.py',uinput],shell=False,stdout=PIPE)
    print(out)

    return render(request,'home.html',{'data1':out.stdout})


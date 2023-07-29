from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def about(request):
   return render(request, 'about/about.html')

def contact(request):
    return render(request, 'contacts/contact.html')
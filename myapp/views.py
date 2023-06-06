from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from .models import Link

# Create your views here.
def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site','')
        print(site)
        
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')
        for link in soup.find_all('a'):
            link_address=link.get('href')
            print(link_address)
            link_text = link.string
            print(link_text)
            Link.objects.create(address = link_address,name = link_text  )
            return HttpResponseRedirect('/')


    else:
        links = Link.objects.all()
    context = {'links': links}
    
    return render(request,'myapp/result.html',context)
def clear(request):
    Link.objects.all().delete()
    return render(request,'myapp/result.html')
    

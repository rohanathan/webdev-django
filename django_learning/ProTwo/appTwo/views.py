from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list}
    return render(request, 'appTwo/index.html', context=date_dict)
    

def help(request):
    helpdict = {'help_me':'HELP PAGE'}
    return render(request, 'help/help.html', context=helpdict)



from django.shortcuts import render
#from appThree.models import User
from appThree.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request, 'appThree/index.html')
                  
def users(request):
    
    form = NewUserForm()
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
            
    return render(request, 'appThree/users.html', {'form':form})
    


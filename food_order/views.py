from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import EditProfileForm

def register_user(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(login_user)
    return render(request, 'food/register.html', {'form': form})

# Create your views here.
def index_page(request):
    return render(request,'food/index.html')


def login_user(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return redirect(index_page)
        else:
            return render(request,'food/login.html',{'message':'Invalid username or password'})
        
    else:
        return render(request,'food/login.html',{'message':'Invalid username or password'}) 
   
def logout_user(request):
    logout(request)
    return redirect(login_user)

def recipes(request):
    return render(request,'food/recipes.html')

def service(request):
    return render(request,'food/services.html')
    
def about(request):
    return render(request,'food/about.html')

def news(request):
    return render(request,'food/news.html')

def single(request):
    return render(request,'food/single.html')

def contact(request):
    return render(request,'food/contact.html')

def edit_profile(request):
    pro=request.user
    if request.method=='POST':
        form =EditProfileForm(request.POST or None,instance=pro)
        if form.is_valid():
 
            form.save()
            return redirect(index_page)
        else:
            form =EditProfileForm(instance=pro)
            return render(request,'food/edit.html',{'form':form,'pro':pro})
    else:
            form =EditProfileForm(instance=pro)
            return render(request,'food/edit.html',{'form':form,'pro':pro})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import City
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddCityForm

# Create your views here.
def home(request):
    return render(request,'index.html')

@login_required(login_url="login")
def explore(request):
    obj=City.objects.all()
    return render(request,'explore.html',{'obj':obj})

@csrf_exempt
def login(request):
    if(request.method=='POST'):
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        user=authenticate(username=user_name, password=pass_word)
        if(user is not None):
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return render(request, "login.html")
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

@csrf_exempt
def register(request):
    if request.method == 'POST':
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        user_name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        if password==password1:
            user=User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)
            user.save()
            print("User created")
            return redirect("/login")
        else:
            messages.info(request, "Password doesn't match")
            return redirect("register")
    else:
        return render(request, "register.html")

def add(request):
    form=AddCityForm()
    return render (request,'add.html',{'form':form})
    
def submitCity(request):
    if(request.method=='POST'):
        form=AddCityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

def manage(request):
    manage=City.objects.all() #reading the data
    return render(request,'manage.html', {'manage': manage})

def edit(request,cid):
    id_new=City.objects.get(id=cid)
    form_new=AddCityForm(request.POST or None,instance=id_new)
    if form_new.is_valid():
            form_new.save()
            return redirect('/manage')
    return render(request,'city_id.html',{'form':form_new,'id':id_new})

    # obj1 = City()
    # obj2=City()
    # obj3=City()
    # obj1.name="Jaipur"
    # obj1.desc="Jaipur is known as a pink city of India. It is situated in Rajasthan. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quaerat rem amet doloribus, ea dolor nemo vitae possimus consectetur repellat aliquam."
    # obj1.days=10
    # obj1.cost=70000
    # obj1.offer=False

    # obj2.name="Bangalore"
    # obj2.desc="Banaglore is known as a pink city of India. It is situated in Rajasthan. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quaerat rem amet doloribus, ea dolor nemo vitae possimus consectetur repellat aliquam."
    # obj2.days=10
    # obj2.cost=70000
    # obj2.offer=True

    # obj3.name="Chennai"
    # obj3.desc="Chennai is known as a pink city of India. It is situated in Rajasthan. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quaerat rem amet doloribus, ea dolor nemo vitae possimus consectetur repellat aliquam."
    # obj3.days=10
    # obj3.cost=70000
    # obj3.offer=False

    # obj=[obj1,obj2,obj3]
    
    
   
   
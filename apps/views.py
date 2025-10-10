from django.shortcuts import render , redirect
from apps.models import Contact
from apps.models import product
from django.contrib.auth import login
from .forms import RegisterForm


#this is for the login 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
   details =  product.objects.all()
   context = {
      'details':details,
   }
   return render(request,'index.html', context)

def details(request,id):
   myproduct = product.objects.all().get(id = id )
   context = {
      'myproduct':myproduct
   }
   return render(request,'details.html',context)

def about(request):
  return render(request,'about.html')

def contact(request):
   if request.method == 'POST':
      email = request.POST.get("email")
      password = request.POST.get("password")
      print(email,password)
      contact = Contact(email = email , password = password)
      contact.save()
   return render(request,'contact.html')


#upload image in the database from the front-end
def upload_product(request):
   if request.method == 'POST':
      title = request.POST.get('title')
      description = request.POST.get('description')
      img = request.FILES.get('img')

      prod = product(title = title , description = description , img = img)
      prod.save()
      context = {
         'title':title
      }
      return render(request,'success.html',context)
   return render(request,'upload_product.html')


#register user form
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


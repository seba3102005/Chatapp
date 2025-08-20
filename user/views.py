from django.shortcuts import render,redirect
from user.forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from .models import ChatRoom
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')


def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])        
            form.save()
            print('registered successfully')
            
            return redirect('login')
            
        else:
            print('something is wrong')
    
    else:
        form = RegisterForm()
    
    context = {'form':form}
    return render(request,'register.html',context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        userr = authenticate(request,username=username,password=password)
        if userr is not None:
        
            login(request,userr)
            return redirect('home') 
        else:
            print('Invalid credentials')
            messages.warning(request,'Invalid Credentials')
            return render(request,'login.html')
        
        
    return render(request,'login.html')

def home(request):
    if request.user.is_authenticated:
        user_chatrooms = ChatRoom.objects.filter(client = request.user)
        context = {'user_chatrooms':user_chatrooms}
        return render(request,'home.html',context)
    else:
        return redirect('login')
    
def logout_view(request):
    logout(request)
    return redirect('login')

def join(request):
    if request.method == 'POST':
        
        room_name = request.POST.get('chatroom')
        
        available_room = ChatRoom.objects.filter(name = room_name).first()
        
        if  available_room is None:
            the_room = ChatRoom.objects.create(name = room_name,owner = request.user)
            the_room.client.add(request.user)

        else:
            available_room.client.add(request.user)        
        return redirect('chatroom',room_name=room_name)
        
    return redirect('chatroom')




def chatroom(request,room_name):
    user_name = request.user.username
    context = {'room_name':room_name,'username':user_name}
    return render(request,'chatroom.html',context)


def delete(request,chat_id):
    if request.method == 'POST':
        chat = ChatRoom.objects.get(id = chat_id)
        if request.user == chat.owner:
            chat.delete()
            messages.success(request,'your chatroom was deleted successfully')

        else:
            messages.warning(request,'you are not authorized to delete this chatroom')

        return redirect('home')
    

def join_again(request,roomID):
    if request.method == 'GET':
        my_room = ChatRoom.objects.all().filter(id = roomID).first()
        return redirect('chatroom',room_name=my_room.name)
    

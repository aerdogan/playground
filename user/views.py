from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']    

        user = auth.authenticate(username=username, password = password)

        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS,'Giriş başarılı.')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR,'Giriş bilgileriniz hatalı!')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS,'Çıkış başarılı.')
        return redirect('index')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING,'Bu kullanıcı adı kayıtlı!')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING,'Bu email daha önce kayıt edilmiş!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password )
                    user.save()
                    messages.add_message(request, messages.SUCCESS,'Kayıt başarılı.')
                    return redirect('login')
        
        else:
            messages.add_message(request, messages.ERROR,'Şifreler aynı olmalı!')

        return redirect('register')
    else:
        return render(request, 'user/register.html')
        
   

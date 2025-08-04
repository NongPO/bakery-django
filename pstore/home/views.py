from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    context = {
        'company_name': 'TechWorld IT Store',
        'description': 'ศูนย์รวมอุปกรณ์ไอทีครบวงจร คอมพิวเตอร์, โน๊ตบุ๊ค, อุปกรณ์เครือข่าย และบริการหลังการขาย',
    }
    return render(request, 'home/index.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'เข้าสู่ระบบสำเร็จ!')
                return redirect('home-index')
            else:
                messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
        else:
            messages.error(request, 'กรุณากรอกชื่อผู้ใช้และรหัสผ่าน')
    
    context = {
        'company_name': 'TechWorld IT Store',
    }
    return render(request, 'home/login.html', context)

def register_view(request):
    context = {
        'company_name': 'TechWorld IT Store',
    }
    return render(request, 'home/register.html', context)
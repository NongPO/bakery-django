from django.shortcuts import render

def index(request):
    context = {
        'company_name': 'TechWorld IT Store',
        'description': 'ศูนย์รวมอุปกรณ์ไอทีครบวงจร คอมพิวเตอร์, โน๊ตบุ๊ค, อุปกรณ์เครือข่าย และบริการหลังการขาย',
    }
    return render(request, 'home/index.html', context)

def login_view(request):
    return render(request, 'home/login.html')

def register_view(request):
    return render(request, 'home/register.html')
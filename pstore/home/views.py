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

def bakery_view(request):
    # เมนูขนมปัง
    menu_items = [
        {
            'name': 'ขนมปังเกลือ',
            'price': 49,
            'original_price': 59,
            'image': 'https://api2.krua.co/wp-content/uploads/2024/07/RB0605_Gallery__Artboard-05.jpg',
            'description': 'หอมกรุ่น นุ่มฟู สดใหม่ทุกวัน',
            'badge': 'NEW!'
        },
        {
            'name': 'ครัวซองต์',
            'price': 55,
            'image': 'https://th.bing.com/th/id/R.94b73325482d70a2f69ea54069d70b6b?rik=41pTPYtBKKXpSA&pid=ImgRaw&r=0',
            'description': 'กรอบนอก นุ่มใน รสชาติฝรั่งเศสแท้'
        },
        {
            'name': 'ขนมปังไส้ทะลัก',
            'price': 59,
            'image': 'https://images.deliveryhero.io/image/fd-th/LH/jkxa-hero.jpg',
            'description': 'ไส้เยอะ หวานมัน อร่อยจนต้องกิน',
            'badge': 'ฮิต!'
        },
        {
            'name': 'ขนมปังลูกเกด',
            'price': 39,
            'image': 'https://th.bing.com/th/id/R.21c2ab065af0dbe45e4f3979850275a4?rik=aslZkLcxRTq0Cg&pid=ImgRaw&r=0',
            'description': 'หวานหอม เคี้ยวเพลิน พร้อมลูกเกดเต็มคำ'
        }
    ]
    return render(request, 'home/category_detail.html', {
        'company_name': 'Bakery Store',
        'category_name': 'ขนมปัง',
        'category_icon': '🍞',
        'menu_items': menu_items
    })

def drinks_view(request):
    # เมนูเครื่องดื่ม
    menu_items = [
        {
            'name': 'อเมริกาโน่',
            'price': 55,
            'image': 'https://th.bing.com/th/id/R.1d8c5b0c0f7e8c8d0cdc9b3e6b7e8c8d?rik=7UxE7KjC8v7vJw&pid=ImgRaw&r=0',
            'description': 'กาแฟเข้มข้น หอมกรุ่น สไตล์อเมริกัน'
        },
        {
            'name': 'คาปูชิโน่',
            'price': 65,
            'image': 'https://th.bing.com/th/id/OIP.Q4XzKVGECKBIL5KgRRJkVAHaHa?rs=1&pid=ImgDetMain',
            'description': 'นมฟองนุ่ม กาแฟหอม รสชาติกลมกล่อม',
            'badge': 'ฮิต!'
        },
        {
            'name': 'ชาเขียวเย็น',
            'price': 45,
            'image': 'https://th.bing.com/th/id/R.1c7c8c8d0cdc9b3e6b7e8c8d0cdc9b3e?rik=7UxE7KjC8v7vJw&pid=ImgRaw&r=0',
            'description': 'ชาเขียวหอมกรุ่น เย็นสดชื่น'
        }
    ]
    return render(request, 'home/category_detail.html', {
        'company_name': 'Bakery Store',
        'category_name': 'เครื่องดื่ม',
        'category_icon': '🥤',
        'menu_items': menu_items
    })

def special_view(request):
    # เมนูลดพิเศษ
    menu_items = [
        {
            'name': 'เซ็ตอาหารเช้า',
            'price': 149,
            'original_price': 189,
            'image': 'https://images.swensen.co.th/uploads/store/Promotion/202406/20240603160012_1.jpg',
            'description': 'อเมริกาโน่ + เฟรนช์โทสต์ + ไส้กรอก',
            'badge': 'โปรพิเศษ!'
        },
        {
            'name': 'เซ็ตขนมหวาน',
            'price': 199,
            'original_price': 249,
            'image': 'https://images.swensen.co.th/uploads/store/Promotion/202406/20240603160012_2.jpg',
            'description': 'เค้กช็อคโกแลต + คาปูชิโน่ + ไอศกรีม',
            'badge': 'ลด 20%'
        }
    ]
    return render(request, 'home/category_detail.html', {
        'company_name': 'Bakery Store',
        'category_name': 'ลดพิเศษ',
        'category_icon': '☕',
        'menu_items': menu_items
    })

def tea_view(request):
    # เมนูชาชัก
    menu_items = [
        {
            'name': 'ชาไทย',
            'price': 35,
            'image': 'https://th.bing.com/th/id/R.1c7c8c8d0cdc9b3e6b7e8c8d0cdc9b3e?rik=7UxE7KjC8v7vJw&pid=ImgRaw&r=0',
            'description': 'ชาไทยหอมกรุ่น หวานมัน รสชาติต้นตำรับ',
            'badge': 'ฮิต!'
        },
        {
            'name': 'ชาเขียวมัทฉะ',
            'price': 55,
            'image': 'https://th.bing.com/th/id/OIP.Q4XzKVGECKBIL5KgRRJkVAHaHa?rs=1&pid=ImgDetMain',
            'description': 'มัทฉะแท้จากญี่ปุ่น หอมหวาน เข้มข้น'
        },
        {
            'name': 'ชาอู่หลง',
            'price': 45,
            'image': 'https://th.bing.com/th/id/R.1d8c5b0c0f7e8c8d0cdc9b3e6b7e8c8d?rik=7UxE7KjC8v7vJw&pid=ImgRaw&r=0',
            'description': 'ชาจีนต้นตำรับ กลิ่นหอมละมุน'
        }
    ]
    return render(request, 'home/category_detail.html', {
        'company_name': 'Bakery Store',
        'category_name': 'ชาชัก',
        'category_icon': '🧊',
        'menu_items': menu_items
    })

def cake_view(request):
    # เมนูเค้ก
    menu_items = [
        {
            'name': 'เค้กช็อคโกแลต',
            'price': 450,
            'image': 'https://th.bing.com/th/id/R.1c7c8c8d0cdc9b3e6b7e8c8d0cdc9b3e?rik=7UxE7KjC8v7vJw&pid=ImgRaw&r=0',
            'description': 'เค้กช็อคโกแลตเข้มข้น 6 นิ้ว สำหรับ 4-6 คน',
            'badge': 'ฮิต!'
        },
        {
            'name': 'เค้กสตรอเบอร์รี่',
            'price': 380,
            'image': 'https://th.bing.com/th/id/OIP.Q4XzKVGECKBIL5KgRRJkVAHaHa?rs=1&pid=ImgDetMain',
            'description': 'เค้กสตรอเบอร์รี่สด หวานซ่า 6 นิ้ว'
        },
        {
            'name': 'เค้กวนิลลา',
            'price': 320,
            'image': 'https://th.bing.com/th/id/R.1d8c5b0c0f7e8c8d0cdc9b3e6b7e8c8d?rik=7UxE7KjC8v7vJw&pid=ImgRaw&r=0',
            'description': 'เค้กวนิลลาคลาสสิค นุ่มละมุน 6 นิ้ว',
            'badge': 'NEW!'
        }
    ]
    return render(request, 'home/category_detail.html', {
        'company_name': 'Bakery Store',
        'category_name': 'เค้ก',
        'category_icon': '🍰',
        'menu_items': menu_items
    })

def recommend_view(request):
    # เมนูแนะนำ
    menu_items = [
        {
            'name': 'ขนมปังเกลือ',
            'price': 49,
            'original_price': 59,
            'image': 'https://api2.krua.co/wp-content/uploads/2024/07/RB0605_Gallery__Artboard-05.jpg',
            'description': 'หอมกรุ่น นุ่มฟู สดใหม่ทุกวัน',
            'badge': 'NEW!'
        },
        {
            'name': 'คาปูชิโน่',
            'price': 65,
            'image': 'https://th.bing.com/th/id/OIP.Q4XzKVGECKBIL5KgRRJkVAHaHa?rs=1&pid=ImgDetMain',
            'description': 'นมฟองนุ่ม กาแฟหอม รสชาติกลมกล่อม',
            'badge': 'ฮิต!'
        },
        {
            'name': 'เค้กช็อคโกแลต',
            'price': 450,
            'image': 'https://th.bing.com/th/id/R.1c7c8c8d0cdc9b3e6b7e8c8d0cdc9b3e?rik=7UxE7KjC8v7vJw&pid=ImgRaw&r=0',
            'description': 'เค้กช็อคโกแลตเข้มข้น 6 นิ้ว สำหรับ 4-6 คน',
            'badge': 'แนะนำ!'
        }
    ]
    return render(request, 'home/category_detail.html', {
        'company_name': 'Bakery Store',
        'category_name': 'แนะนำ',
        'category_icon': '⭐',
        'menu_items': menu_items
    })
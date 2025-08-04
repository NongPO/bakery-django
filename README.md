# 🧁 Bakery Django Project

เว็บไซต์ร้านขนมปังและเบเกอรี่ที่พัฒนาด้วย Django

## 🚀 วิธีการติดตั้งและรัน

### 1. Clone โปรเจ็ค
```bash
git clone https://github.com/yourusername/bakery-django.git
cd bakery-django
```

### 2. สร้าง Virtual Environment

#### ใช้ Python venv
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### ใช้ Conda
```bash
conda create --name bakery-django python=3.10
conda activate bakery-django
```

### 3. ติดตั้ง Dependencies
```bash
cd pstore
pip install -r requirements.txt
```

### 4. รัน Database Migration
```bash
python manage.py migrate
```

### 5. รัน Development Server
```bash
python manage.py runserver
```

เปิดเบราว์เซอร์แล้วไปที่: `http://127.0.0.1:8000/`

## 🌐 Deploy ไปยัง PythonAnywhere

### 1. สร้างบัญชี PythonAnywhere
- ไปที่ [PythonAnywhere](https://www.pythonanywhere.com/)
- สมัครสมาชิก (Free tier ก็เพียงพอ)

### 2. อัปโหลดโค้ด
```bash
# ใน PythonAnywhere Console
git clone https://github.com/NongPO/bakery-django.git
cd bakery-django
```

### 3. สร้าง Virtual Environment
```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

### 4. ติดตั้ง Dependencies
```bash
cd pstore
pip install -r requirements.txt
```

### 5. ตั้งค่า Web App
1. ไปที่ **Web** tab ใน Dashboard
2. กด **Add a new web app**
3. เลือก **Manual configuration** > **Python 3.10**
4. ตั้งค่า **Source code** path: `/home/yourusername/bakery-django/pstore`
5. ตั้งค่า **WSGI configuration file**

### 6. แก้ไข WSGI file
```python
import os
import sys

# Add your project directory to sys.path
path = '/home/yourusername/bakery-django/pstore'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'bakery_django.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 7. ตั้งค่า Static Files
- **URL**: `/static/`
- **Directory**: `/home/yourusername/bakery-django/pstore/staticfiles/`

### 8. รัน Migration และ Collect Static
```bash
cd /home/yourusername/bakery-django/pstore
python manage.py migrate
python manage.py collectstatic
```

### 9. Reload Web App
กด **Reload** button ใน Web tab

เว็บไซต์จะพร้อมใช้งานที่: `https://yourusername.pythonanywhere.com`

## 🛠️ เทคโนโลยีที่ใช้

- Django 4.2.7
- Bootstrap 5
- SQLite (Development)
- Whitenoise (Static Files)

## 📁 โครงสร้างโปรเจ็ค

```
bakery-django/
├── pstore/
│   ├── manage.py
│   ├── requirements.txt
│   ├── bakery_django/     # Settings และ URLs หลัก
│   └── home/              # Templates และ Views
└── .venv/                 # Virtual Environment
```

## 🎯 Features

- หน้าแรกร้านขนมปัง
- ระบบโปรโมชั่น
- UI/UX ที่สวยงาม
- Responsive Design

# 🧁 Bakery Django Project

เว็บไซต์ร้านขนมปังและเบเกอรี่ที่พัฒนาด้วย Django

## 🚀 วิธีการติดตั้งและรัน

### 1. Clone โปรเจ็ค
```bash
git clone https://github.com/yourusername/bakery-django.git
cd bakery-django
```

### 2. สร้าง Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate
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

# 🏎️ SRIPATUM GARAGE - Car Rental System

ยินดีต้อนรับสู่ **Sripatum Garage** ระบบเช่ารถออนไลน์ระดับพรีเมียม พัฒนาโดยนักศึกษาจากมหาวิทยาลัยศรีปทุม (SPU) 
หน้าเว็บมาในสไตล์ Dark Mode ตัดด้วยแสงนีออนชมพู ให้ความรู้สึก Modern และ High-end

## 👥 ผู้จัดทำ (Developed By)
- **ชื่อ-นามสกุล:** [นาย พงศภัค เสทิน 68076288]
- **ชื่อ-นามสกุล:** [นาย บรรณวัชร บุญเปลี่ยม 68083112]
- **ชื่อ-นามสกุล:** [นางสาว เรืองทอง สุดโต 68077841]
- **คณะ:** เทคโนโลยีสารสนเทศ (SIT)
- **มหาวิทยาลัย:** มหาวิทยาลัยศรีปทุม (SPU)

## ✨ Features (ความสามารถของระบบ)
- **Car List:** แสดงรายการรถทั้งหมดที่พร้อมให้เช่า
- **Booking System:** ระบบจองรถผ่าน Modal พร้อมระบบคำนวณวันและเช็กสถานะ
- **My Bookings:** หน้าแสดงประวัติการจองรถของผู้ใช้งาน
- **Admin Dashboard:** จัดการข้อมูลรถและดูรายการจองทั้งหมดผ่านระบบหลังบ้านของ Django
- **Static & Media:** ระบบจัดการรูปภาพพื้นหลังโปรเจกต์และรูปภาพรถที่อัปโหลด

## 🚀 วิธีติดตั้งและรันโปรเจกต์ (How to Install)

1. **ติดตั้ง Library ที่จำเป็น:**
```bash
pip install -r requirements.txt
สร้างฐานข้อมูล:

Bash
python manage.py migrate
สร้างรหัส Admin (Superuser):

Bas้
python manage.py createsuperuser
รันเซิร์ฟเวอร์:

Bash
python manage.py runserver
📁 โครงสร้างโฟลเดอร์ที่สำคัญ
cars/: แอปพลิเคชันหลักของระบบ

static/images/: ที่เก็บไฟล์รูปภาพพื้นหลัง (j1.jpg)

media/: ที่เก็บรูปภาพรถที่อัปโหลดผ่านหน้า Admin

templates/: หน้า HTML ทั้งหมดของระบบ

### 📸 ตัวอย่างหน้าจอการทำงาน (Screenshots)

#### 1. หน้าแสดง Welcome (Home Page)
<img width="1906" height="1017" alt="home" src="https://github.com/user-attachments/assets/5123f1b5-4e43-44c4-8572-832afc4f4fb9" />
<img width="1899" height="1020" alt="home2" src="https://github.com/user-attachments/assets/329fabbe-4d35-49b8-8181-5944f5a6ba2e" />

#### 2. หน้าแสดงรายการรถ (Car Inventory)
<img width="1899" height="1020" alt="home2" src="https://github.com/user-attachments/assets/596a463d-f6c0-43cc-8f28-a1f627aa9922" />
<img width="1886" height="1017" alt="carlist" src="https://github.com/user-attachments/assets/62710ac4-8bc4-4a61-a582-2d18ec88bf6d" />

#### 3. หน้าแสดงการจองสำเร็จ (Booking Success)
<img width="1900" height="1020" alt="22" src="https://github.com/user-attachments/assets/b4fd4bda-389a-43bc-b247-27c1bff1470c" />
<img width="1894" height="1020" alt="33" src="https://github.com/user-attachments/assets/8d3c8503-8c6b-48d4-8507-64bca97c6ed9" />

#### 4. หน้าจัดการข้อมูลหลังบ้าน (Admin Panel)
<img width="1904" height="1018" alt="admin" src="https://github.com/user-attachments/assets/ceba3044-1e84-480e-b2af-929a07d13d15" />
<img width="1904" height="1020" alt="admin2" src="https://github.com/user-attachments/assets/12a0d724-9e6b-4824-9fb5-1b7fda223ed8" />

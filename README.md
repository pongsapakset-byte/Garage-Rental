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

#### 1. หน้าแสดงWelcome (Home Page)
<img width="1906" height="1017" alt="Screenshot 2026-04-16 235120" src="https://github.com/user-attachments/assets/67309127-afda-4f2d-b2c6-9a8dee1bf6b5" />

#### 2. หน้าแสดงรายการรถ (Home Page)
<img width="1899" height="1020" alt="Screenshot 2026-04-16 235149" src="https://github.com/user-attachments/assets/21e17662-67ec-4cdf-bc92-fca36333ba45" />
<img width="1886" height="1017" alt="Screenshot 2026-04-16 235205" src="https://github.com/user-attachments/assets/f5aaf575-0eca-4e4b-ab77-8f1e15795e17" />
<img width="1890" height="1019" alt="Screenshot 2026-04-16 235213" src="https://github.com/user-attachments/assets/4181a703-183e-407d-8fa6-83f65766133b" />


#### 3. หน้าแสดงการจองสำเร็จ (Booking Success)
<img width="1900" height="1020" alt="Screenshot 2026-04-17 000525" src="https://github.com/user-attachments/assets/a780847f-b8e2-46bb-8a96-1346139da67b" />
<img width="1894" height="1020" alt="Screenshot 2026-04-17 000559" src="https://github.com/user-attachments/assets/a7b7bad5-fc00-40e6-8ffa-1f66fa329a9a" />

#### 4. หน้าจัดการข้อมูลหลังบ้าน (Admin Panel)
<img width="1904" height="1018" alt="Screenshot 2026-04-16 235407" src="https://github.com/user-attachments/assets/678460ca-eecf-4ec6-b93a-c8792be7f429" />
<img width="1904" height="1020" alt="Screenshot 2026-04-16 235421" src="https://github.com/user-attachments/assets/b6de1fe2-c91d-468d-8066-c45cc141847d" />




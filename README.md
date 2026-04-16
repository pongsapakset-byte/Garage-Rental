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
<img width="1906" height="1017" alt="Screenshot 2026-04-16 235120" src="https://github.com/user-attachments/assets/fc972c6f-654d-449f-b690-cd65eef9e5b6" />
<img width="1890" height="1019" alt="Screenshot 2026-04-16 235213" src="https://github.com/user-attachments/assets/80e77678-6dd6-4898-9bda-8a75ff9c35d7" />

#### 2. หน้าแสดงรายการรถ (Home Page)
<img width="1899" height="1020" alt="Screenshot 2026-04-16 235149" src="https://github.com/user-attachments/assets/8720128f-a43a-40d5-9dc2-182f34abe678" />
<img width="1886" height="1017" alt="Screenshot 2026-04-16 235205" src="https://github.com/user-attachments/assets/81b952f0-494e-4942-b4ac-422c84c8828a" />

#### 3. หน้าแสดงการจองสำเร็จ (Booking Success)
<img width="1900" height="1020" alt="Screenshot 2026-04-17 000525" src="https://github.com/user-attachments/assets/14a35571-e0e6-4c7a-a1f8-122415339bcf" />
<img width="1894" height="1020" alt="Screenshot 2026-04-17 000559" src="https://github.com/user-attachments/assets/6e898f38-fa43-49f7-844c-9fce519eea1e" />

#### 4. หน้าจัดการข้อมูลหลังบ้าน (Admin Panel)
<img width="1904" height="1018" alt="Screenshot 2026-04-16 235407" src="https://github.com/user-attachments/assets/e1385bc1-9af2-4756-90cf-46290cbe4e76" />
<img width="1904" height="1020" alt="Screenshot 2026-04-16 235421" src="https://github.com/user-attachments/assets/2df54127-8225-46d7-bf4e-049e10ed16c8" />



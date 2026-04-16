from django.contrib import admin
from .models import Car, Booking

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # โชว์ข้อมูลรถ: แบรนด์, ชื่อรุ่น, ราคาต่อวัน, จำนวนที่นั่ง
    list_display = ('brand', 'name', 'price_per_day', 'seats')
    # เพิ่มช่องค้นหารถจากชื่อหรือแบรนด์
    search_fields = ('brand', 'name')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # 🚨 จุดสำคัญ: โชว์รายชื่อลูกค้า, รถที่จอง, วันเริ่ม-วันจบ, และยอดเงินรวม 72,000 (สำหรับ Ferrari)
    list_display = ('customer_name', 'car', 'start_date', 'end_date', 'total_price')
    
    # เพิ่มตัวกรอง (Filter) ด้านขวามือให้มึงเช็กงานง่ายขึ้น
    list_filter = ('car', 'start_date')
    
    # สั่งให้ยอดเงินรวมเป็น Read Only (ดูได้อย่างเดียว ห้ามแก้เพื่อให้เลขมันตรงตามสูตร)
    readonly_fields = ('total_price',)

# หมายเหตุ: กูเอา admin.site.register เดิมออกแล้วเปลี่ยนมาใช้ @admin.register แทน 
# เพื่อความเท่และจัดระเบียบคอลัมน์ได้แม่นยำกว่าเดิม
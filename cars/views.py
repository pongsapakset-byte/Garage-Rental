from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Car, Booking
import datetime

# 🔥 หน้าแรก (HOME)
def home(request):
    return render(request, 'home.html')

# 🔥 หน้ารายการรถ
def car_list(request):
    cars = Car.objects.all()

    brand_query = request.GET.get('brand', '')
    price_query = request.GET.get('price', '')

    if brand_query:
        cars = cars.filter(
            Q(brand__icontains=brand_query) |
            Q(name__icontains=brand_query)
        )

    if price_query:
        try:
            price_query = float(price_query)
            cars = cars.filter(price_per_day__lte=price_query)
        except:
            pass

    return render(request, 'car_list.html', {'cars': cars})

# 🔥 ฟังก์ชันจองรถ
def book_car(request, id):
    car = get_object_or_404(Car, id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        start_str = request.POST.get('start')
        end_str = request.POST.get('end')

        try:
            sd = datetime.datetime.strptime(start_str, '%Y-%m-%d').date()
            ed = datetime.datetime.strptime(end_str, '%Y-%m-%d').date()

            if ed < sd:
                messages.error(request, "วันคืนรถต้องมากกว่าวันรับรถ")
                return redirect(request.META.get('HTTP_REFERER', '/'))

            days = (ed - sd).days + 1
            total_price = days * car.price_per_day

            # ✅ กูเพิ่ม total_price เข้าไปตรงนี้ เพื่อให้ยอดเงินบันทึกลงหน้า Admin
            Booking.objects.create(
                customer_name=name,
                car=car,
                start_date=sd,
                end_date=ed,
                total_price=total_price  # <--- จุดที่เพิ่ม
            )

            messages.success(
                request,
                f"จอง {car.name} สำเร็จ! ({days} วัน) รวม {total_price:,.0f} บาท"
            )

        except Exception as e:
            messages.error(request, f"การจองผิดพลาด: {str(e)}")

        return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('car_list')

# 🔥 หน้า My Bookings
def my_bookings(request):
    bookings = Booking.objects.all().order_by('-id')
    return render(request, 'my_bookings.html', {'bookings': bookings})
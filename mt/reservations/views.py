from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation, Table
from .forms import ReservationForm
from django.contrib import messages

def reservation_create(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            table = form.cleaned_data['table']
            date = form.cleaned_data['date']
            customer = form.cleaned_data['customer']

            # Проверяем, есть ли уже бронь на этот столик в эту дату
            existing_reservation = Reservation.objects.filter(table=table, date=date).exists()
            user_existing_reservation = Reservation.objects.filter(customer=customer, date=date).exists()

            if existing_reservation:
                messages.error(request, "Этот столик уже забронирован на выбранную дату!")
            elif user_existing_reservation:
                messages.error(request, "У вас уже есть бронь на этот день!")
            else:
                form.save()
                messages.success(request, "Бронь успешно создана!")
                return redirect("reservation_list")  # Перенаправление на список броней
    else:
        form = ReservationForm()

    return render(request, "reservations/reservation_form.html", {"form": form})

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, 'reservations/reservation_detail.html', {'reservation': reservation})



def reservation_edit(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/reservation_edit.html', {'form': form})

def reservation_delete(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_delete.html', {'reservation': reservation})
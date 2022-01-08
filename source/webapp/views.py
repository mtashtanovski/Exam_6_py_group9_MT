from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from webapp.models import Guest, STATUS_CHOICES


def index_view(request):
    guests = Guest.objects.order_by('-updated_at')
    return render(request, 'index.html', {'guests': guests})


def add_note(request, ):
    if request.method == 'GET':
        return render(request, 'add_note.html', {"status_choices": STATUS_CHOICES})
    else:
        guest_name = request.POST.get('guest_name')
        guest_mail = request.POST.get('guest_mail')
        guest_text = request.POST.get('guest_text')
        new_note = Guest.objects.create(guest_name=guest_name, guest_mail=guest_mail, guest_text=guest_text)
        return redirect('index')


def update_note(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == "GET":
        return render(request, 'update_note.html', {'guest': guest})
    else:
        guest.guest_name = request.POST.get('guest_name')
        guest.guest_mail = request.POST.get('guest_mail')
        guest.guest_text = request.POST.get('guest_text')
        guest.save()
        return redirect('index')


def delete_note(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == "GET":
        return render(request, 'delete_note.html', {'guest': guest})
    else:
        guest.delete()
        return redirect('index')

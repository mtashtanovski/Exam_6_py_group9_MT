from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from webapp.models import Guest, STATUS_CHOICES


def index_view(request):
    guests = Guest.objects.order_by('-created_at')
    return render(request, 'index.html', {'guests': guests})

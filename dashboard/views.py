from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages

from item.models import Item


@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })
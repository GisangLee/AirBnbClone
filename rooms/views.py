from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render
from . import models


class HomeView(ListView):
    """ Home View Definition """

    model = models.Room
    paginate_by = 10
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", context={"room": room})
    
    except models.Room.DoesNotExist:
        raise Http404()


from django.shortcuts import render

def index(request):
    return render(request, 'chat_body/index.html')
# Create your views here.
def room(request, room_name):
    return render(request, 'chat_body/room.html', {
        'room_name': room_name
    })
from django.shortcuts import render
from .models import Message

def index(request):
    ctx = {
        'messages': Message.objects.all(),
    }
    if request.method == "POST":
        new_message_text = request.POST['text']
        Message.objects.create(text=new_message_text)

    return render(request, 'index.html', ctx)

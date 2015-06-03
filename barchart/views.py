from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from .models import Message
from django.contrib.auth.models import User


def index(request):
    ctx = {
        'messages': Message.objects.all(),
    }
    # print(ctx['messages'])
    if request.method == "POST":
        if request.user.is_authenticated():
            new_message_text = request.POST['text']
            Message.objects.create(
                author=request.user,
                text=new_message_text)
        else:
            raise PermissionDenied()

    return render(request, 'index.html', ctx)


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .forms import SigninForm
import json

from .play import Gameplay

def index(request):
    return HttpResponse(status=200)

def get_name(request):
    print("IN GET NAME")
    print(request.method)
    print(request.body)
    print("DONE")
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session['name'] = name
            gameplay = Gameplay()
            gameplay.addPlayer(name)
            player = gameplay.getPlayer(name)
            #send message to websocket
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)("players", {"type": "game.message", "message": player})
            return HttpResponseRedirect('/gameplay/')
    else:
        form = SigninForm()

    return render(request, 'gameplay/signinForm.html', {'form': form})

        # playerDict = json.loads(request.body)
        # request.session['name'] = playerDict['name']
        # gameplay = Gameplay()
        # gameplay.addPlayer(playerDict['name'])
        #
        # return HttpResponse(json.dumps({'name': request.session['name']}), status=200,  content_type="application/json" )


def gameState(request):
    gameplay = Gameplay()
    players = gameplay.getOrder()
    myPlayer = gameplay.getPlayer(request.session['name'])
    context = {
        'myPlayer': myPlayer,
        'players': players,
    }
    return render(request, 'gameplay/gameplay.html', context)
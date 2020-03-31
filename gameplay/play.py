import json
from django.core import serializers
from .cardDeck import CardDeck
from .models import Player

class Gameplay():
    def __init__(self):
        self.cardDeck = CardDeck()
    def addPlayer(self, name):
        dealtCards = self.cardDeck.dealTwo()
        turn = len(Player.objects.all()) + 1
        player = Player.objects.create(name=name, income_action='Income: 1 coin', foreign_aid_action='Foreign Aid: Take 2 Coins (Can be blocked by duke)', coins=2, card1=dealtCards[0], card2=dealtCards[1], state="PENDING", turn=turn)
        player.save()

    def getOrder(self):
        order = []
        players = Player.objects.all()
        for player in players:
            order.append(self.getPlayer(player.name))
        return order


    def getPlayer(self, playerName):
        player = Player.objects.get(name=playerName)
        myPlayer = {
            'name': player.name,
            'coins': player.coins,
            'card1': player.card1.type,
            'card2': player.card2.type
        }
        return myPlayer

    def getPlayerCoins(self, playerName):
        player = self.getMyPlayer(playerName)
        return player.coins



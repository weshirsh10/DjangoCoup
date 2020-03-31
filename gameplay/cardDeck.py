import random
from django.core import serializers
from .models import Card


class CardDeck():
    def __init__(self):
        self.cardDeck = Card.objects.all()

    def dealTwo(self):
        card1 = random.choice(Card.objects.filter(state='DECK'))
        card1.state = "DEALT"
        card1.save()
        card2 = random.choice(Card.objects.filter(state='DECK'))
        card2.state = "DEALT"
        card2.save()
        return [card1, card2]

    def exchangeCards(self, card1In, card2In):
        card1In.state = 'DECK'
        card1In.save()
        card2In.state = 'DECK'
        card2In.save()
        return self.dealTwo()

    def cardSerializer(self, card):
        card1 = serializers.serialize('json', Card.objects.filter(pk=card))
        print("card1", card1)

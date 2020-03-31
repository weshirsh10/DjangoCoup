from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Card(models.Model):
    type = models.CharField(max_length=20)
    action = models.CharField(max_length=20)
    counteraction = models.CharField(max_length=20)
    state = models.CharField(max_length=10)

    def __str__(self):
        return self.type

class Player(models.Model):
    name = models.CharField(max_length=20)
    income_action = models.CharField(max_length=20)
    foreign_aid_action = models.CharField(max_length=20)
    coins = models.IntegerField()
    card1 = models.ForeignKey(Card,  on_delete=models.DO_NOTHING, related_name='%(class)s_requests_created')
    card1State = models.CharField(max_length=20)
    card2 = models.ForeignKey(Card,  on_delete=models.DO_NOTHING)
    card2State = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    turn = models.IntegerField()

    def __str__(self):
        return self.name


    def delete(self, using=None, keep_parents=False):
        self.card1.state = 'DECK'
        self.card2.state = 'DECK'
        self.card1.save()
        self.card2.save()
        print("DELETING", self.name)
        super().delete()

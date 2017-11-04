from django.db import models
from django.db.models import Sum
from django.core.validators import MaxValueValidator, MinValueValidator

from django.utils.translation import ugettext as _


class Team(models.Model):
    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
        
    def get_team_goals(self):
        return Player.objects.filter(team__name=self.name).aggregate(Sum('goals'))
        
    def get_team_players(self):
        return Player.objects.filter(team__name=self.name).count()

    def get_stats(self):
        exp = Player.objects.filter(team__name=self.name).aggregate(Sum('experience'))
        score = self.get_team_goals()
        try:
            return score['goals__sum']/exp['experience__sum']
        except TypeError:
            return 0
        

class Player(models.Model):
    class Meta:
        verbose_name = _('Player')
        verbose_name_plural = _('Players')
        
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
        ],
        help_text=_('From 1 to 100')
        )
    height = models.PositiveIntegerField(validators=[
        MinValueValidator(40),
        MaxValueValidator(500)
        ],
        help_text=_('In cm. From 40 to 500')
        )
    experience = models.PositiveIntegerField()
    goals = models.PositiveIntegerField()
    team = models.ForeignKey('Team', related_name="team")
    
    def __str__(self):
        return self.name

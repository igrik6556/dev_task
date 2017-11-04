from django.views.generic import ListView
from statistic.models import Team, Player


class TeamsList(ListView):
    model = Team
    template_name = "statistic/teams.html"
    context_object_name = 'teams'


class PlayersList(ListView):
    model = Player
    template_name = "statistic/players.html"
    context_object_name = 'players'

    def get_queryset(self):
        qs = super(PlayersList, self).get_queryset()
        return qs.filter(team__id=int(self.kwargs["pk"]))

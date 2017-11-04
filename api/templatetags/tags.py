from django import template
from statistic.models import Team, Player

register = template.Library()


@register.inclusion_tag("api/_api_nav.html")
def api_navigation():
    list_teams = Team.objects.all()
    list_players = Player.objects.all()
    return {'list_teams': list_teams, 'list_players': list_players}

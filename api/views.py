from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from statistic.models import Team, Player
from api.serializers import (
    TeamSerializer,
    PlayerSerializer,
    TeamCreateSerializer,
    PlayerCreateSerializer,
    )


class TeamListAPIView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
	

class PlayerListAPIView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

	
class TeamDetailAPIView(RetrieveAPIView):
    lookup_url_kwarg = 'teamId'
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
	
    
class PlayerDetailAPIView(RetrieveAPIView):
    lookup_url_kwarg = 'playerId'
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    
class TeamCreateAPIView(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateSerializer

    
class PlayerCreateAPIView(CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerCreateSerializer
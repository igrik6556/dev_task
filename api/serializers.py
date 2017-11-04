from rest_framework.serializers import ModelSerializer, CharField
from statistic.models import Team, Player


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'city']
		
	
class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'age', 'height', 'experience', 'goals', 'team']
       
       
class TeamCreateSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'city']
       
       
class PlayerCreateSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['name', 'age', 'height', 'experience', 'goals', 'team']
        
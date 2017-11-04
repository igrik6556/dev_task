from django.conf.urls import url
from api.views import (
    TeamListAPIView,
    PlayerListAPIView,
    TeamDetailAPIView,
    PlayerDetailAPIView,
    TeamCreateAPIView,
    PlayerCreateAPIView,
    )

urlpatterns = [
    url(r'^teams/$', TeamListAPIView.as_view(), name='teams-api'),
    url(r'^players/$', PlayerListAPIView.as_view(), name='players-api'),
    url(r'^teams/(?P<teamId>\d+)/$', TeamDetailAPIView.as_view(), name='team-api'),
    url(r'^players/(?P<playerId>\d+)/$', PlayerDetailAPIView.as_view(), name='player-api'),
    url(r'^team/$', TeamCreateAPIView.as_view(), name='create-team-api'),
    url(r'^player/$', PlayerCreateAPIView.as_view(), name='create-player-api'),
]

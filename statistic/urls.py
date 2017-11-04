from django.conf.urls import url
from statistic.views import TeamsList, PlayersList

urlpatterns = [
    url(r'^$', TeamsList.as_view(), name="stats"),
    url(r'^players/team-(?P<pk>\d+)/$', PlayersList.as_view(), name="players"),
]

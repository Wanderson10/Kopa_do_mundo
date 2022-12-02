from django.urls import path
from .views import TeamView,TeamIdViews


urlpatterns = [
    path('teams/',TeamView.as_view()),
    path('teams/<int:team_id>/', TeamIdViews.as_view())
]

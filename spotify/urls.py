from django.urls import path
from . import views

urlpatterns = [
    path('get-auth-url', views.AuthURL.as_view()),
    path('redirect', views.spotify_callback),
    path('is-authenticated', views.IsAuthenticated.as_view()),
    path('current-song', views.CurrentSong.as_view()),
    path('spotify-tokens', views.SpotifyModelView.as_view()),
    path('clear-spotify-tokens', views.ClearSpotifyTokens.as_view()),
]

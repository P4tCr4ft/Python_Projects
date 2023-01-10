from django.urls import path, include
from watchlist_app.api.views import StreamPlatformDetailAV, StreamPlatformAV, WatchListAV, WatchDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('list/<int:pk>', WatchDetailAV.as_view(), name='watch_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
]
